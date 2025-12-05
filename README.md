XY Linked List Cloning in Python

This repository contains an implementation of a custom linked list data structure where each node has two pointers:

X pointer (similar to next in a singly linked list)

Y pointer (an additional reference that can point to any node in the list)

The project demonstrates how to deep clone such a complex linked list while preserving both pointer relationships.

Features

XYNode class implementing a node with:

data

x_pointer

y_pointer

Creation of a sample linked list with defined X and Y relationships

A three-step cloning process:

Interleave clone nodes within original list

Copy Y pointers to the cloned nodes

Extract the cloned list from the interleaved structure

Visualization function to print both lists

File Overview
XYNode Class

Defines a node with getters and setters for data, X pointer, and Y pointer.

clone_xy_list(head)

Clones the list by interweaving cloned nodes between original nodes.

add_y_pointers(head)

Sets Y pointers for each cloned node by referencing corresponding clones.

extract_cloned_list(head)

Separates the merged list into:

Restored original list

Fully cloned list

visualize_xy_list(head)

Prints each node along with its X and Y pointer relationships.

Example Output

Running the script will show:

Original list

List after inserting clone nodes and setting Y pointers

Final extracted:

Restored original list

Deep-cloned list

Each output shows every node and its X/Y references.
