#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number to a list
 * @head:pointer to pointer to a head node
 * @number:the number to be inserted
 *
 *
 * Return:the adress of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *old;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	old = *head;

	while (old->next != NULL && old->next->n < number)
	{
		old = old->next;
	}
	new->next = old->next;
	old->next = new;
	return(new);
}
