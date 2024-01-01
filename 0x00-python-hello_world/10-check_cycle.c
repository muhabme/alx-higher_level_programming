#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: Pointer to the head of a singly-linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *a, *b;

    if (!list || !(list->next))
        return (0);

    a = list->next;
    b = list->next->next;

    while (a && b && b->next)
    {
        if (a == b)
            return (1);

        a = a->next;
        b = b->next->next;
    }

    return (0);
}
