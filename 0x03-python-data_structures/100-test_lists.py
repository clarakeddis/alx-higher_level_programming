from collections.abc import Sized
import ctypes
from xml.dom.minidom import Element

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
julien@ubuntu:~/CPython$ python3 100-test_lists.py  # type: ignore
Sized of the Python List = 2 # type: ignore
Allocated = 2
Element 0: str # type: ignore
Element 1: str # type: ignore
Sized of the Python List = 1 # type: ignore
Allocated = 2
Element 0: str # type: ignore
Sized of the Python List = 7 # type: ignore
Allocated = 7
Element 0: str # type: ignore
Element 1: int # type: ignore
Element 2: int # type: ignore
Element 3: float # type: ignore
Element 4: tuple # type: ignore
Element 5: list # type: ignore
Element 6: str # type: ignore
Sized of the Python List = 0 # type: ignore
Allocated = 0
Sized of the Python List = 1 # type: ignore
Allocated = 4
Element 0: int # type: ignore
Sized of the Python List = 5 # type: ignore
Allocated = 8
Element 0: int # type: ignore
Element 1: int # type: ignore
Element 2: int # type: ignore
Element 3: int # type: ignore
Element 4: int # type: ignore
Sized of the Python List = 4 # type: ignore
Allocated = 8
Element 0: int # type: ignore
Element 1: int # type: ignore
Element 2: int # type: ignore
Element 3: int # type: ignore
