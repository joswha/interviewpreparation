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

llist1 = LinkedList(["7", "1", "6"])
llist2 = LinkedList(["5", "9", "2"])

def addLists(llist1, llist2):
    return sumLists(llist1, llist2, 0)

def sumLists(llist1, llist2, carry):
    if(llist1 == None and llist2 == None and carry == 0):
        return None
    
    result = LinkedList()
    value = carry

    if llist1 != None:
        value += llist1.data
    
    if llist1 != None:
        value += llist2.data

    result.data = value % 10

    if llist1 != None or llist2 != None:
        more = sumLists(None if llist1 == None else llist1.next, None if llist2 == None else llist2.next, 1 if value >= 10 else 0)
        result.next = more

    return result

print(addLists(llist1, llist2))