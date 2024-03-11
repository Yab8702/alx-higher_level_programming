#include "lists.h"


/**
  * check_cycle - checks if a singly linked list has a cycle in it.
  * @list: list
  * Return: 0(No cycle) | 1(has cycle)
  */


int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	fast = slow = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
