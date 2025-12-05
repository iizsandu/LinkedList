# Overview

Cloning a linked list with arbitrary cross-references requires careful pointer handling. A naive approach becomes inefficient or requires extra space.
This project implements a well-known three-step method to clone the list in:

O(n) time

O(1) extra space

The steps include inserting cloned nodes within the original list, setting correct Y references, and separating the cloned list from the original.

## How the Cloning Algorithm Works
### 1. Interleave clones with original nodes

Each original node gets its clone inserted immediately after it:

Original1 → Clone1 → Original2 → Clone2 → ...

### 2. Set Y pointers of cloned nodes

Because clone nodes follow their originals, a cloned Y pointer can be assigned by referencing:

clone.y = original.y.x

### 3. Extract the cloned list

The interleaved structure is split back into two independent lists:

Restored original list

Fully functional cloned list

Code Structure
XYNode

A node with:

data

x_pointer

y_pointer

Includes getter and setter methods for clarity.

clone_xy_list(head)

Creates clone nodes and interleaves them with original nodes.

add_y_pointers(head)

Assigns the Y pointer for each cloned node based on the structure created in step 1.

extract_cloned_list(head)

Separates the original list and the cloned list.

visualize_xy_list(head)

Prints each node's data and the data pointed to by its X and Y pointers.
