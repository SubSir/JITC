# JITC
一个简单的LLVM JIT编译器

## **简化的 LLVM 语法**
对LLVM语法进行了简化和约束，具体见[语法文档](docs/grammar.md)

## **启动**
主文件为`src/interpreter.py`，运行后命令行输入命令，执行结果在命令行输出。

## **JIT逻辑**
这是一个函数级粗粒度的JIT编译器。`main`函数作为入口会用解释器运行，其他函数满足以下条件会被JIT编译：
1. 函数调用次数大于`CALL_TIMES`(位于`src/interpreter.py`中)
2. 该函数不会调用内建函数`@printstr`(见[语法文档](docs/grammar.md))。

示例可见[call.ll](testcases/call.ll)、[function.ll](testcases/function.ll)、[function2.ll](testcases/function2.ll)、[str.ll](testcases/str.ll)、[str2.ll](testcases/str2.ll)