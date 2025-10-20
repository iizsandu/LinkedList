# A class for node with two pointers

class XYNode:
    def __init__(self, data=None,  x_pointer=None, y_pointer = None):
        self.__data = data
        self.__x_pointer = x_pointer
        self.__y_pointer = y_pointer

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data

    def get_x(self):
        return self.__x_pointer
    
    def set_x(self, x):
        self.__x_pointer = x

    def get_y(self):
        return self.__y_pointer
    
    def set_y(self, y):
        self.__y_pointer = y


# creating a linked list
head = XYNode(1)
node2 = XYNode(2)
node3 = XYNode(3)
node4 = XYNode(4)
node5 = XYNode(5)

head.set_x(node2)
node2.set_x(node3)
node3.set_x(node4)
node4.set_x(node5)
node5.set_x(None)

head.set_y(node3)
node2.set_y(node4)
node3.set_y(head)
node4.set_y(node5)
node5.set_y(node3)

def clone_xy_list(head):

    temp = head
    while temp is not None:
        clone_node = XYNode(temp.get_data())
        clone_node.set_x(temp.get_x())
        temp.set_x(clone_node)

        temp = clone_node.get_x()
    
    return head

# def traverse_x(head):
#     temp = head
#     while temp is not None:
#         print(temp.get_data(), end="->")
#         temp = temp.get_x()

def add_y_pointers(head):
    temp = head

    while temp is not None:
        y_pointer = temp.get_y()
        cloned_temp = temp.get_x()
        cloned_temp.set_y(y_pointer.get_x())

        temp = cloned_temp.get_x()
    
    return head

def extract_cloned_list(head):
    temp = head
    clone_head = head.get_x()
    temp2 = clone_head

    while temp is not None and temp2 is not None:

        if temp2.get_x() is None:
            temp.set_x(None)
            temp2.set_x(None)
            break

        next_temp = temp2.get_x() 
        temp.set_x(next_temp)
        temp2.set_x(next_temp.get_x())

        temp = next_temp
        temp2 = temp.get_x()

    return head, clone_head

def visualize_xy_list(head):
    temp = head
    while temp is not None:
        data = temp.get_data()

        x_data = temp.get_x().get_data() if temp.get_x() else None
        y_data = temp.get_y().get_data() if temp.get_y() else None

        print(f"Node({data}) -> X: {x_data}, Y: {y_data}")

        temp = temp.get_x()

if __name__ == "__main__":
    print("\n Original list")
    visualize_xy_list(head)

    cloned = clone_xy_list(head)
    add_y_pointers(cloned)
    print("\n After adding the clones and the y pointers")
    visualize_xy_list(cloned)

    original, clone = extract_cloned_list(cloned)
    print("\n Original list after extraction") 
    visualize_xy_list(original)
    print("\n Cloned list after extraction")
    visualize_xy_list(clone)
