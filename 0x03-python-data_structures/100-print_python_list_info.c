#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - checks if a linked list is a palindrome
 * @p: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
