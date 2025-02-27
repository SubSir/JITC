import mmap
import ctypes

# 分配一块可读、可写、可执行的内存区域
def allocate_executable_memory(size):
    return mmap.mmap(-1, size, prot=mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC)

# RISC-V 指令对应的机器码（32-bit 指令）
machine_code = bytearray([
    0x33, 0x05, 0xb5, 0x00,  # add a0, a0, a1
    0x67, 0x80, 0x00, 0x00   # ret
])

# 分配可执行内存
exec_mem = allocate_executable_memory(len(machine_code))

# 将机器码写入内存
exec_mem.write(machine_code)

# 将内存指针转换为可调用的函数
# 假设函数签名是 int func(int a, int b)
func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func_ptr = ctypes.cast(ctypes.addressof(ctypes.c_int.from_buffer(exec_mem)), func_type)

# 调用函数
result = func_ptr(10, 20)  # 相当于执行 a0 = 10, a1 = 20, 返回 a0 + a1
print("Result:", result)

# 释放内存
exec_mem.close()