#include <pybind11/pybind11.h>

#include <iostream>
namespace py = pybind11;

// 强制16字节对齐(足够满足大多数架构)
#ifdef _MSC_VER
#define ALIGNED_FUNCTION __declspec(align(16))
#else
#define ALIGNED_FUNCTION __attribute__((aligned(16)))
#endif

static py::function global_py_callback;
static bool python_running = true;

void set_global_callback(py::function py_callback) {
  py::gil_scoped_acquire acquire;
  global_py_callback = py_callback;
}

extern "C" ALIGNED_FUNCTION void* trampoline_to_python(intptr_t a0, intptr_t a1,
                                                       intptr_t a2, intptr_t a3,
                                                       intptr_t a4, intptr_t a5,
                                                       intptr_t a6,
                                                       intptr_t a7) {
  // std::cout << "trampoline_to_python" << std::endl;
  if (!python_running || global_py_callback.is_none()) {
    return nullptr;
  }

  py::gil_scoped_acquire acquire;

  try {
    py::tuple py_args = py::make_tuple(a0, a1, a2, a3, a4, a5, a6, a7);
    py::object result = global_py_callback(*py_args);

    if (!result.is_none()) {
      intptr_t int_result = result.cast<intptr_t>();
      return reinterpret_cast<void*>(int_result);
    }
  } catch (py::error_already_set& e) {
    std::cerr << "Python error: " << e.what() << std::endl;
    PyErr_Print();
  }

  return nullptr;
}

uintptr_t get_trampoline_address() {
  // 确保返回的地址是对齐的
  uintptr_t addr = reinterpret_cast<uintptr_t>(&trampoline_to_python);
  if (addr % 16 != 0) {
    std::cerr << "Warning: Trampoline address is not properly aligned: " << addr
              << std::endl;
  }
  return addr;
}

PYBIND11_MODULE(trampoline, m) {
  m.def("get_trampoline_address", &get_trampoline_address,
        "获取trampoline_to_python函数的内存地址");

  m.def("set_global_callback", &set_global_callback, "设置全局Python回调函数");

  m.add_object("_cleanup", py::capsule([]() {
                 py::gil_scoped_acquire acquire;
                 python_running = false;
                 global_py_callback = py::function();
               }));
}