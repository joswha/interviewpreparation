##################################################################################################### 
#                                      SKELETON CODE                                                #
##################################################################################################### 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

def size(llist):
    k = 0
    for node in llist:
        k+=1
    return k

def empty(llist):
    return llist.head is None

def value_at(llist, index):
    k = 0
    for node in llist:
        if k == index:
            return node
        k+=1

def push_front(llist, value):
    new_node = Node(value)
    new_node.next = llist.head
    llist.head = new_node
    return llist

def pop_front(llist):
    cop = llist.head
    llist.head = cop.next
    return cop

def push_back(llist, value):
    new_node = Node(value)
    for node in llist:
        if node.next is None:
            node.next = new_node
            new_node.next = None
    return llist

def pop_back(llist):
    for node in llist:
        if (node.next).next is None:
            cop = node.next
            node.next = None
    return cop
            
def front(llist):
    return llist.head

def back(llist):
    for node in llist:
        if node.next is None:
            return node

def insert(llist, index, value):
    k = 0
    for node in llist:
        if k == index - 1:
            cp = node.next
            node.next = Node(value)
            (node.next).next = cp
        k = k + 1

def erase(llist, index):
    k = 0
    for node in llist:
        if k == index - 1:
            cp = (node.next).next
            node.next = cp
        k += 1

def value_n_from_end(llist, n):
    size_l = size(llist)
    k = 0
    for node in llist:
        if size_l - k == n:
            return node
        k += 1

def reverse(llist):
    reversed_llist = LinkedList()
    for node in llist:
        if node is not None:
            push_front(reversed_llist, str(node))
    return reversed_llist

def remove_value(llist, value):
    k = 0
    for node in llist:
        if str(node) == value:
            erase(llist, k)
        k += 1

#####################################################################################################
##################################################################################################### 

llist = LinkedList(["4", "1", "3", "5", "8", "7"])

# Write code to partition a linked list around a value x, such that all nodes less than xcome brefore all nodes greater than or equal to x

def partition(llist, x):
    elems_list = [int(str(i)) for i in llist]
    less_list = []
    greater_list = []

    for elem in elems_list:
        if elem < x:
            less_list.append(elem)
        else:
            greater_list.append(elem)
        
    less_list = [str(i) for i in less_list]
    greater_list = [str(i) for i in greater_list]

    llist = LinkedList(less_list + greater_list)

    print(llist)
    # print(less_list, greater_list)

partition(llist, 5)