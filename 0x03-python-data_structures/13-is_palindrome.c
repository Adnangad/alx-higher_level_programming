#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * rev_list - iterates a list in reverse
 * @head:pointer to head node
 *
 * Return:the list in reverse
 */
listint_t *rev_list(listint_t *head)
{
	listint_t *prev, *curent, *nextnode;

	prev = NULL;
	curent = head;
	nextnode = NULL;

	while (curent != NULL)
	{
		nextnode = curent->next;
		curent->next = prev;
		prev = curent;
		curent = nextnode;
	}
	return (prev);
}
/**
 * is_palindrome -checks whether a list is palindrome
 * @head:point to point of head
 *
 * Return:0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (0);
	}
	listint_t *cur, *rev = rev_list(*head);

	cur = *head;

	if (rev == NULL)
	{
		return (0);
	}
	while (cur != NULL && rev != NULL)
	{
		if (cur->n != rev->n)
		{
			return (0);
		}
		cur = cur->next;
		rev = rev->next;
	}
	return (1);
}
