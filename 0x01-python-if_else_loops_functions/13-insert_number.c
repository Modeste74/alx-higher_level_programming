#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - it inserts node to alreay existing list
 * @head: pointer to a pointerto the head
 * @number: number to be insert in the list
 *
 * Return: address on new node and NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *before = NULL, *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return NULL;

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head->n))
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current != NULL && current->n < number)
	{
		before = current;
		current = current->next;
	}
	before->next = new;
	new->next = current;
	return (new);
}
