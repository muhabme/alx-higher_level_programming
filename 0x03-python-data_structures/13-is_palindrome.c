#include "lists.h"

/**
 * reverse_linked_list - Reverses the order of nodes in a singly linked list.
 * @head: Reference to the head pointer of the list.
 */
void reverse_linked_list(listint_t **head)
{
    listint_t *previous = NULL;
    listint_t *current_node = *head;
    listint_t *next_node = NULL;

    while (current_node != NULL)
    {
        next_node = current_node->next;
        current_node->next = previous;
        previous = current_node;
        current_node = next_node;
    }

    *head = previous;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 *
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head, *fast_ptr = *head;
    listint_t *first_half = *head, *second_half = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    while (fast_ptr != NULL && fast_ptr->next != NULL)
    {
        fast_ptr = fast_ptr->next->next;
        slow_ptr = slow_ptr->next;
    }

    if (fast_ptr != NULL)
        second_half = slow_ptr->next;
    else
        second_half = slow_ptr;

    reverse_linked_list(&second_half);

    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
            return 0;
        first_half = first_half->next;
        second_half = second_half->next;
    }

    return 1;
}
