#include <Python.h>

/**
* print_python_list_info - prints some basic info about pytohn list
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = list->allocated;
	PyObject *item;
	Py_ssize_t i;
	const char *item_type;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, item_type);
	}
}
