#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome -checks whether a list is palindrome
 * @head:point to point of head
 *
 * Return:0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{
	listint_t *current  = *head;
	int i, length = 0;

	while (current != NULL)
	{
		length++;
		current = current->next;
	}
	int arr[length];
	current = *head;

	for (i = 0; i < length; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}
	for (i = 0; i < length / 2; i++)
	{
		if (arr[i] != arr[length - i - 1])
		{
			return (0);
		}
	}
	return (1);
}
