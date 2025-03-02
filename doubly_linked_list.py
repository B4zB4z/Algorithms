#doubly linked lists
# null<-[p|d|n]-><-[p|d|n]-><-[p|d|n]->null
#[p|d|n] = node
# p = previous (a pointer that points to the previous Node)
# d = data (data is stored here)
# n = next (a pointer that points to the next Node)


# define a Node
class Node():
    def __init__(self, data):
        #data stored in the node
        self.data = data
        #previous pointer 
        self.prev = None
        #next pointer
        self.next = None

#define the double linked list
class DoubleLinkedList():
    def __init__(self):
        #head is the start of the list, previous node is always Null
        self.head = None
        #tail is the end of the list, next node is always null
        self.tail = None

    #function to add nodes in the list
    def add(self, value):
        new_node = Node(value)
        #if list is empty new node gets both pointers of head and tail
        if self.head is None:
            self.head = self.tail = new_node
        #if there is a node already, the previous pointer of the new node will point to the head
        #the next pointer of the head will point to the new node
        #and the new node will get the pointer of the tail, pointing at it 
        else:
            new_node.prev = self.head
            self.head.next = new_node
            self.tail = new_node
    

    def display(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next
    



