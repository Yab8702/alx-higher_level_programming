#include "lists.h"


/**
 * insert_node - insert a new node into soreted linked list
 * @head: head of the list
 * @number: the number to be inserted
 * Return: @new_node | NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node;
	listint_t *prev;
	int num;

	if (head == NULL || *head == NULL)
		return (NULL);
	while (current != NULL)
	{
		num = current->n;
		if (number < num)
		{
			new_node = malloc(sizeof(listint_t));
			if (new_node == NULL)
				return (NULL);
			new_node->next = current;
			new_node->n = number;
			prev->next = new_node;
			break;

		}
		prev = current;
		current = current->next;
	}
	return (*head);
}
