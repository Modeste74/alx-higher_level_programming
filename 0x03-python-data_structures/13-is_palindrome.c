#include "lists.h"

/**
 * is palindrone - checks if singly linked list is a palindrome
 * @head: pointer to a pointer to the first node
 *
 * Return: 1 if it, else 0
 */
int is_palindrome(listint_t **head)
{
	int array[500];
	listint_t *current;
	int n, count = 0;

	current = *head;
	while (current != NULL)
	{
		array[count++] = current->n;
		current = current->next;
	}
	for (n = 0; n < count / 2; n++)
	{
		if (array[n] != array[count - n -1])
			return (0);
	}
	return (1);
}
