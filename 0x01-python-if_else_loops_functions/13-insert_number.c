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
	listint_t *prev = current;
	int num;

	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		(*head) = malloc(sizeof(listint_t));
		(*head)->next = NULL;
		(*head)->n = number;
	}
	while (current != NULL)
	{
		num = current->n;
		if ((number < num) || (current->next == NULL))
		{
			new_node = malloc(sizeof(listint_t));
			if (new_node == NULL)
				return (NULL);
			if (current->next == NULL)
			{
				new_node->next = NULL;
				prev = current;
			}
			else
				new_node->next = current;
			new_node->n = number;
			if (number < (*head)->n)
				*head = new_node;
			else
				prev->next = new_node;
			break;

		}
		prev = current;
		current = current->next;
	}
	return (*head);
}
