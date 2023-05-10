#include "lists.h"

/**
 * check_cycle - checks if a list has cycle
 * @list: pointer to head of the linked list
 *
 * Return: 1 if present and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *hide, *seek;

	if (list == NULL)
		return (0);

	hide = seek = list;
	while (seek != NULL && seek->next != NULL)
	{
		hide = hide->next;
		seek = seek->next->next;
		if (hide == seek)
			return (1);
	}
	return (0);
}
