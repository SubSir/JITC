import hex
import asm
import mmap
import ctypes


def allocate_executable_memory(size):
    return mmap.mmap(-1, size, prot=mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC)


def exec(func_ptr, param_list, stack_top):
    param_list = [stack_top] + param_list
    return func_ptr(*param_list)


class Function:
    def __init__(self, machine_code, return_type, param_types, memory):
        self.exec_mem = memory
        self.exec_mem.write(machine_code)
        if return_type == "void":
            return_type = None
        elif return_type == "i64" or return_type == "i1":
            return_type = ctypes.c_int
        else:
            raise Exception("Invalid return type: {}", return_type)

        param_types = [
            ctypes.c_int if (param_type == "i64" or param_type == "i1") else None
            for param_type in param_types
        ]
        param_types = [ctypes.c_uint64] + param_types
        func_type = create_func_type(return_type, param_types)
        self.mem_address = ctypes.addressof(ctypes.c_uint64.from_buffer(self.exec_mem))
        self.func_ptr = ctypes.cast(self.mem_address, func_type)

    def exec(self, param_list, stack_top):
        param_list = [stack_top] + param_list
        return self.func_ptr(*param_list)


def allocate_stack_memory(size=4096):
    stack_mem = mmap.mmap(-1, size, prot=mmap.PROT_READ | mmap.PROT_WRITE)
    stack_base = ctypes.addressof(ctypes.c_uint64.from_buffer(stack_mem))
    stack_top = (stack_base + size) & ~0xF
    return stack_top


class Stack:
    def __init__(self, size=4096):
        self.stack_mem = mmap.mmap(-1, size, prot=mmap.PROT_READ | mmap.PROT_WRITE)
        stack_base = ctypes.addressof(ctypes.c_uint64.from_buffer(self.stack_mem))
        self.stack_top = (stack_base + size) & ~0xF


def create_func_type(return_type, param_types):
    return ctypes.CFUNCTYPE(return_type, *param_types)


def byte2mem(machine_code: bytearray, return_type: str, param_types: list, memory):
    return Function(machine_code, return_type, param_types, memory)


def code2func(code: str, global_info=None) -> Function:
    asm_code, func = asm.main(code)
    size = len(asm_code.splitlines()) * 4 * 2
    memory = allocate_executable_memory(size)
    address = ctypes.addressof(ctypes.c_uint64.from_buffer(memory))
    func = func[0]
    for i in range(6, -1, -1):
        asm_code = asm_code.replace("a" + str(i), "a" + str(i + 1))
    insert = asm_code.find(":\n")
    asm_code = asm_code[: insert + 2] + "\tmv sp, a0\n" + asm_code[insert + 2 :]
    asm_code = asm_code.replace("_", "a0")
    # print(asm_code)
    hex_code = hex.asm_to_bytearray(asm_code, global_info, address)

    func = byte2mem(hex_code, func[0], func[1], memory)

    return func


def main(code: str):
    asm_code, func = asm.main(code)
    size = len(asm_code.splitlines()) * 4
    memory = allocate_executable_memory(size)
    address = ctypes.addressof(ctypes.c_uint64.from_buffer(memory))
    func = func[0]
    for i in range(6, -1, -1):
        asm_code = asm_code.replace("a" + str(i), "a" + str(i + 1))
    insert = asm_code.find(":\n")
    asm_code = asm_code[: insert + 2] + "\tmv sp, a0\n" + asm_code[insert + 2 :]
    asm_code = asm_code.replace("_", "a0")
    print(asm_code)
    hex_code = hex.asm_to_bytearray(asm_code)

    func = byte2mem(hex_code, func[0], func[1], memory)

    stack = Stack()

    result = exec(func.func_ptr, [1, 2], stack.stack_top)

    print(result)


if __name__ == "__main__":
    code = """define i64 @add(i64 %a, i64 %b) {
        .ret:
          %c = add i64 %a, %b 
          ret i64 %c 
        }"""
    main(code)
