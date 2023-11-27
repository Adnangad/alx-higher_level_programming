#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singley linked ist has a cycle in it
 * @list:the list
 * 
 *
 * Return:0 if no cycle,1 if theres a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *y;

	if (list->next == NULL || list == NULL)
	{
		return (0);
	}
	x = list;
	y = list->next;

	while(x && y && y->next->next)
	{
		if (x == y)
		{
			return (1);
		}
		x = x->next;
		y = y->next->next;
	}
	return (0);
}
