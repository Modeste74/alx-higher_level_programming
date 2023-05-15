#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	int i, size;
	PyListObject *list;
	PyObject *obj;

	size = Pylist_Size(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
