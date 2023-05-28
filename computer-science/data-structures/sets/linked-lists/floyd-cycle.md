## Floyd Cycle Finding Algorithm (Hare-Tortoise)

A pointer algorithm that uses only two poitners (slow and fast), moving through the sequence at different speeds. This algorithm is used to find a loop in a linked list.

While traversing the linked list:

- Fast pointer may reach the end (NULL) and no cycle is found
- Fast pointer catches the slow pointer at some time and cycle is found

### Pseudo

- Initialize two pointers
- Move slow pointer by one position
- Move fast pointer by two positions
- If both points meet at some point, a cycle exists
