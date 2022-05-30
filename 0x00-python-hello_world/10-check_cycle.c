#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1
 */

int check_cycle(listint_t *list)
{
	listint_t *mother, *father;

	if (list == NULL || list->next == NULL)
		return (0);

	mother = list->next;
	father = list->next->next;

	while (mother && father && father->next)
	{
		if (mother == father)
			return (1);

		mother = mother->next;
		father = father->next->next;
	}
	return (0);
}
