#include "lists.h"
/**
 * print_dlistint - Function that prints all elements of a list
 * @h: pointer to header
 * Return: return elements
 */
size_t print_dlistint(const dlistint_t *h)
{
	int nodes;

	nodes = 0;

	if (h == NULL)
		return (nodes);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		nodes++;
		h = h->next;
	}

	return (nodes);
}
