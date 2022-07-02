# Linked lists in Python

[Linked lists](https://www.educative.io/blog/data-structures-linked-list-java-tutorial) are a sequential collection of data that uses **relational pointers on each data node** to link to the next node in the list.

Unlike arrays, linked lists do not have objective positions in the list. Instead, they have relational positions based on their surrounding nodes.

The first node in a linked list is called the **head node**, and the final is called the tail node, which has a `null` pointer.

Linked lists can be singly or doubly linked depending if each node has just a single pointer to the next node or if it also has a second pointer to the previous node.

## Applications:

- Building block for *advanced data structures*

- Solutions that call for frequent *addition and removal of data*

## Common linked list interview questions in Python:

- *Print the middle element* of a given linked list

- *Remove duplicate elements* from a sorted linked list

- Check if a singly linked list is a *palindrome*

- *Merge K sorted linked lists*

- *Find the intersection point* of two linked lists

# Circular linked lists in Python

The primary downside of the standard linked list is that you always have to start at the Head node.

The circular linked list fixes this problem by replacing the Tail node’s `null` pointer with a pointer **back to the Head node**. When traversing, the program will follow pointers until it reaches the node it started on.

The advantage of this setup is that you can start at any node and traverse the whole list. It also allows you to use linked lists as a loop-able structure by setting a desired number of cycles through the structure.

Circular linked lists are great for processes that loop for a long time like CPU allocation in operating systems.

## Applications:

- Regularly looping solutions like CPU scheduling

- Solutions where you want the freedom to start traversal at any node

## Common circular linked list interview questions in Python

- *Detect loop* in a linked lists

- *Reverse* a circular linked list

- *Reverse circular linked list in groups of give size*
