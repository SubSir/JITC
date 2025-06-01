# setup.py
from setuptools import setup, Extension
import platform

# 获取pybind11包含路径
import pybind11

ext_modules = [
    Extension(
        "trampoline",
        ["trampoline.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=[
            "-std=c++11" if platform.system() != "Windows" else "/std:c++14"
        ],
    ),
]

setup(
    name="trampoline",
    version="0.1",
    ext_modules=ext_modules,
)
