# size() - returns number of data elements in list
# empty() - bool returns true if empty
# value_at(index) - returns the value of the nth item (starting at 0 for first)
# push_front(value) - adds an item to the front of the list
# pop_front() - remove front item and return its value
# push_back(value) - adds an item at the end
# pop_back() - removes end item and returns its value
# front() - get value of front item
# back() - get value of end item
# insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
# erase(index) - removes node at given index
# value_n_from_end(n) - returns the value of the node at nth position from the end of the list
# reverse() - reverses the list
# remove_value(value) - removes the first item in the list with this value
# https://realpython.com/linked-lists-python/#implementing-your-own-linked-list

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

llist = LinkedList(["a", "b", "c", "d", "e"])
# reversed_llist = LinkedList()
reversed_llist = reverse(llist)
remove_value(llist, "c")
# push_front(llist, "x")
print(llist)
print(reversed_llist)
# insert(llist, 4, "y")
# erase(llist, 1)
# print(value_n_from_end(llist, 3))
# pop_back(llist)
# print(front(llist))
# print(value_at(llist,2))
