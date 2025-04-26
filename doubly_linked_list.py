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
        #if there is a node already, the previous pointer of the new node will point to the current tail
        #the next pointer of the current tail will point to the new node
        #and the new node will become the new tail 
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    #function to display the list
    def display(self):
        #we start from the beggining of the list (head), and we print everything with a while loop
        #moving the pointer to the next node until it becomes none
        pointer = self.head
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next
    
    #function to remove a node from the list
    def remove(self, value):
        pointer = self.head
        while pointer is not None:
            #if it's the first element
            if value == pointer.data and pointer == self.head:
                self.head = self.head.next
                self.head.prev = None
            #if it's the last element
            elif pointer == pointer.data and pointer == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            #if there is only one element in the list
            elif pointer == self.head and pointer == self.tail:
                self.head = self.tail = None
            #if it's in the middle
            elif pointer == value:
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
            return True
        pointer = pointer.next
        return False
    







list = DoubleLinkedList()
list.add(3)
list.add(24)
list.add(9)
list.add(786)
list.add(75)
list.add(35)
list.add(6)
list.display()
list.remove(6)
list.display()
