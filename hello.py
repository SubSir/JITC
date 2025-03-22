import mmap
import ctypes

# 分配一块可读、可写、可执行的内存区域
def allocate_executable_memory(size):
    return mmap.mmap(-1, size, prot=mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC)


# RISC-V 指令对应的机器码
machine_code = bytearray(
    [
  0x13, 0x01, 0x05, 0x00, 0x13, 0x8a, 0x00, 0x00, 0x13, 0x01, 0x01, 0xfe, 0x23, 0x30, 0x11, 0x00, 0x23, 0x34, 0x81, 0x00, 0x23, 0x38, 0x91, 0x00, 0x13, 0x84, 0x05, 0x00, 0x93, 0x04, 0x06, 0x00, 0x33, 0x04, 0x94, 0x00, 0x13, 0x05, 0x04, 0x00, 0x83, 0x30, 0x01, 0x00, 0x93, 0x8a, 0x00, 0x00, 0x03, 0x34, 0x81, 0x00, 0x83, 0x34, 0x01, 0x01, 0x13, 0x01, 0x01, 0x02, 0x67, 0x80, 0x00, 0x00,
  ])# 分配可执行内存
exec_mem = allocate_executable_memory(4096)

# 将机器码写入内存
exec_mem.write(machine_code)

# 将内存指针转换为可调用的函数
# 假设函数签名是 int func(int a)
# 假设我们在运行时得到了参数类型
def create_func_type(return_type, param_types):
    """
    动态生成 CFUNCTYPE
    :param return_type: 返回值类型 (如 ctypes.c_int)
    :param param_types: 参数类型列表 (如 [ctypes.c_uint64, ctypes.c_int])
    :return: CFUNCTYPE 对象
    """
    return ctypes.CFUNCTYPE(return_type, *param_types)

# 示例：动态创建 CFUNCTYPE
param_types = [ctypes.c_uint64, ctypes.c_int, ctypes.c_int]  # 参数类型
return_type = ctypes.c_int  # 返回类型
func_type = create_func_type(return_type, param_types)
func_ptr = ctypes.cast(ctypes.addressof(ctypes.c_int.from_buffer(exec_mem)), func_type)

mem_address = ctypes.addressof(ctypes.c_uint64.from_buffer(exec_mem))

print(f"Memory address: 0x{mem_address:x}")

# 分配栈空间 
stack_mem = mmap.mmap(-1,  4096, prot=mmap.PROT_READ | mmap.PROT_WRITE)
stack_base = ctypes.addressof(ctypes.c_uint64.from_buffer(stack_mem)) 
stack_top = (stack_base + 4096) & ~0xF  # 强制16字节对齐的栈顶地址 
print(f"Valid stack range: 0x{stack_base:x} ~ 0x{stack_top:x}")
 
# 调用时传入合法栈地址 
result = func_ptr(stack_top, 2, 1)

# 调用函数
print("Result:", result)

# 释放内存
exec_mem.close()
