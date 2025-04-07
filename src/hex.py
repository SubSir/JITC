def encode_r_type(inst, rd, rs1, rs2):
    opcode, funct3, funct7 = instruction_set[inst]
    return f"{funct7}{reg_to_bin(rs2)}{reg_to_bin(rs1)}{funct3}{reg_to_bin(rd)}{opcode}"


def encode_i_type(inst, rd, rs1, imm):
    opcode, funct3 = instruction_set[inst]
    imm_bin = imm_to_bin(imm, 12)
    return f"{imm_bin}{reg_to_bin(rs1)}{funct3}{reg_to_bin(rd)}{opcode}"


def encode_s_type(inst, rs1, rs2, imm):
    opcode, funct3 = instruction_set[inst]
    imm_bin = imm_to_bin(imm, 12)
    return (
        f"{imm_bin[:7]}{reg_to_bin(rs2)}{reg_to_bin(rs1)}{funct3}{imm_bin[7:]}{opcode}"
    )


def encode_b_type(inst, rs1, rs2, imm):
    opcode, funct3 = instruction_set[inst]
    imm_bin = imm_to_bin(imm, 13)
    return (
        f"{imm_bin[0]}{imm_bin[2:8]}{reg_to_bin(rs2)}{reg_to_bin(rs1)}"
        f"{funct3}{imm_bin[8:12]}{imm_bin[1]}{opcode}"
    )


def encode_u_type(inst, rd, imm):
    opcode = instruction_set[inst][0]
    imm_bin = imm_to_bin(imm, 20)
    return f"{imm_bin}{reg_to_bin(rd)}{opcode}"


def encode_j_type(inst, rd, imm):
    opcode = instruction_set[inst][0]
    imm_bin = imm_to_bin(imm, 21)
    return (
        f"{imm_bin[0]}{imm_bin[10:20]}{imm_bin[9]}{imm_bin[1:9]}"
        f"{reg_to_bin(rd)}{opcode}"
    )


registers = {
    "zero": 0,
    "ra": 1,
    "sp": 2,
    "gp": 3,
    "tp": 4,
    "t0": 5,
    "t1": 6,
    "t2": 7,
    "s0": 8,
    "fp": 8,
    "s1": 9,
    "a0": 10,
    "a1": 11,
    "a2": 12,
    "a3": 13,
    "a4": 14,
    "a5": 15,
    "a6": 16,
    "a7": 17,
    "s2": 18,
    "s3": 19,
    "s4": 20,
    "s5": 21,
    "s6": 22,
    "s7": 23,
    "s8": 24,
    "s9": 25,
    "s10": 26,
    "s11": 27,
    "t3": 28,
    "t4": 29,
    "t5": 30,
    "t6": 31,
}

instruction_set = {
    "add": ("0110011", "000", "0000000"),
    "sub": ("0110011", "000", "0100000"),
    "and": ("0110011", "111", "0000000"),
    "or": ("0110011", "110", "0000000"),
    "xor": ("0110011", "100", "0000000"),
    "sll": ("0110011", "001", "0000000"),
    "srl": ("0110011", "101", "0000000"),
    "sra": ("0110011", "101", "0100000"),
    "slt": ("0110011", "010", "0000000"),
    "sltu": ("0110011", "011", "0000000"),
    "addi": ("0010011", "000"),
    "andi": ("0010011", "111"),
    "ori": ("0010011", "110"),
    "xori": ("0010011", "100"),
    "slli": ("0010011", "001", "0000000"),
    "srli": ("0010011", "101", "0000000"),
    "srai": ("0010011", "101", "0100000"),
    "slti": ("0010011", "010"),
    "sltiu": ("0010011", "011"),
    "lb": ("0000011", "000"),
    "lh": ("0000011", "001"),
    "lw": ("0000011", "010"),
    "ld": ("0000011", "011"),
    "lbu": ("0000011", "100"),
    "lhu": ("0000011", "101"),
    "sb": ("0100011", "000"),
    "sh": ("0100011", "001"),
    "sw": ("0100011", "010"),
    "sd": ("0100011", "011"),
    "beq": ("1100011", "000"),
    "bne": ("1100011", "001"),
    "blt": ("1100011", "100"),
    "bge": ("1100011", "101"),
    "bltu": ("1100011", "110"),
    "bgeu": ("1100011", "111"),
    "jal": ("1101111",),
    "jalr": ("1100111", "000"),
    "auipc": ("0010111",),
    "lui": ("0110111",),
}


def reg_to_bin(reg):
    return f"{registers[reg]:05b}"


def imm_to_bin(imm, length):
    imm = int(imm)
    if imm < 0:
        imm = (1 << length) + imm
    return f"{imm:0{length}b}"[-length:]


def record_labels(asm, pc=0):
    labels = {}
    lines = asm.splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("."):
            continue
        if line.endswith(":"):
            labels[line[:-1]] = pc
        else:
            pc += 4
    return labels


def expand_pseudo_instructions(asm, labels, pc):
    expanded = []
    lines = asm.splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith(".") or line.endswith(":"):
            expanded.append(line)
            continue

        parts = line.split()
        inst = parts[0]
        args = [arg.strip(",") for arg in parts[1:]]

        if inst == "mv":
            expanded.append(f"addi {args[0]}, {args[1]}, 0")
        elif inst == "li":
            imm = int(args[1])
            if -2048 <= imm <= 2047:
                expanded.append(f"addi {args[0]}, zero, {imm}")
            else:
                upper = (imm + (1 << 11)) >> 12
                lower = imm - (upper << 12)
                expanded.append(f"lui {args[0]}, {upper}")
                expanded.append(f"addi {args[0]}, {args[0]}, {lower}")
                pc += 4
        elif inst == "la":
            label = "@" + args[1]
            address = labels[label] - pc
            top_20 = (address + (1 << 11)) >> 12
            low_12 = address - (top_20 << 12)
            expanded.append(f"auipc {args[0]}, {top_20}")
            expanded.append(f"addi {args[0]}, {args[0]}, {low_12}")
            pc += 4
        elif inst == "call":
            label = args[0]
            address = labels[label] - pc
            top_20 = (address + (1 << 11)) >> 12
            low_12 = address - (top_20 << 12)
            expanded.append(f"addi a0, sp, 0")
            expanded.append(f"auipc t0, {top_20}")
            expanded.append(f"addi t0, t0, {low_12}")
            expanded.append(f"jalr ra, t0, 0")
            pc += 12
        elif inst == "ret":
            expanded.append("jalr zero, ra, 0")
        else:
            expanded.append(line)
        pc += 4

    return "\n".join(expanded)


def process_instructions(asm, labels, pc=0):
    machine_code = []
    lines = asm.splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith(".") or line.endswith(":"):
            continue

        parts = line.split()
        inst = parts[0]
        args = [arg.strip(",") for arg in parts[1:]]
        if len(args) > 1 and "(" in args[1]:
            args.append(args[1].split("(")[0])
            args[1] = args[1].split("(")[1].split(")")[0]

        if inst in instruction_set:
            if inst in {
                "add",
                "sub",
                "and",
                "or",
                "xor",
                "sll",
                "srl",
                "sra",
                "slt",
                "sltu",
            }:
                mc = encode_r_type(inst, args[0], args[1], args[2])
            elif inst in {
                "addi",
                "andi",
                "ori",
                "xori",
                "slli",
                "srli",
                "srai",
                "slti",
                "sltiu",
                "jalr",
            }:
                mc = encode_i_type(inst, args[0], args[1], args[2])
            elif inst in {"lb", "lh", "lw", "lbu", "lhu", "ld"}:
                mc = encode_i_type(inst, args[0], args[1], args[2])
            elif inst in {"sb", "sh", "sw", "sd"}:
                mc = encode_s_type(inst, args[1], args[0], args[2])
            elif inst in {"beq", "bne", "blt", "bge", "bltu", "bgeu"}:
                offset = (labels[args[2]] - pc) // 4
                mc = encode_b_type(inst, args[0], args[1], offset)
            elif inst in {"lui", "auipc"}:
                mc = encode_u_type(inst, args[0], args[1])
            elif inst in {"jal"}:
                if len(args) == 1:
                    args.insert(0, "ra")
                offset = (labels[args[1]] - pc) // 4
                mc = encode_j_type(inst, args[0], offset)
            else:
                raise ValueError(f"Unknown instruction: {inst}")
            machine_code.append(f"{int(mc, 2):08x}")
            pc += 4
        else:
            raise ValueError(f"Unknown instruction: {inst}")

    return "\n".join(machine_code)


def asm_to_hex(asm):
    labels = record_labels(asm)

    expanded_asm = expand_pseudo_instructions(asm, labels)

    machine_code = process_instructions(expanded_asm, labels)

    for line in machine_code.splitlines():
        for i in range(len(line) - 2, -1, -2):
            print(f"0x{line[i:i+2]},", end=" ")
        print()


def asm_to_bytearray(asm: str, global_info=None, pc=0) -> bytearray:
    labels = record_labels(asm, pc)

    if global_info is not None:
        for key, value in global_info.items():
            labels[key] = value

    expanded_asm = expand_pseudo_instructions(asm, labels, pc)

    machine_code = process_instructions(expanded_asm, labels, pc)

    byte_list = []

    for line in machine_code.splitlines():
        for i in range(len(line) - 2, -1, -2):
            byte_list.append(int(line[i : i + 2], 16))
    return bytearray(byte_list)


if __name__ == "__main__":
    asm_code = """.text
.globl add
add:
        mv sp, a0
        addi sp, sp, -32
        sd ra, 0(sp)
        sd s0, 8(sp)
        sd s1, 16(sp)
        mv s0, a1
        mv s1, a2
add.ret:
        add s0, s0, s1
        mv a0, s0
        ld ra, 0(sp)
        ld s0, 8(sp)
        ld s1, 16(sp)
        addi sp, sp, 32
        ret
.data
    """

    asm_to_hex(asm_code)
