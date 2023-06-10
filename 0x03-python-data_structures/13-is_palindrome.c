#include "lists.h"


/**
 * reverse_list - reverse a half singly linked list
 * @head: the head pointer
 * Return: the reverse list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL, *current = head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: the head pointer
 * Return: 1(if its palindrome) | 0(if not)
 */


int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *first_half, *second_half, *second_half_rev;

	if (head == NULL || *head == NULL)
		return (1);
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	second_half_rev = reverse_list(slow->next);
	first_half = *head;
	second_half = second_half_rev;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
