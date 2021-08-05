# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedList = LinkedList(0) # dummy initial pointer
    currentNode = newLinkedList
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne else 0
        valueTwo = nodeTwo.value if nodeTwo else 0

        temp_sum = valueOne + valueTwo + carry
        new_value = temp_sum % 10
        carry = temp_sum // 10

        newNode = LinkedList(new_value)
        currentNode.next = newNode
        currentNode = newNode

        nodeOne = nodeOne.next if nodeOne else None
        nodeTwo = nodeTwo.next if nodeTwo else None

    return newLinkedList.next # skip dummy initial pointer
    
    
    
    
    
    
    # # Write your code here.
    # array_one = []
    # array_two = []
    # res = []

    # while linkedListOne != None:
    #     array_one.append(linkedListOne.value)
    #     linkedListOne = linkedListOne.next
    
    # while linkedListTwo != None:
    #     array_two.append(linkedListTwo.value)
    #     linkedListTwo = linkedListTwo.next

    # min_length = min(len(array_one), len(array_two))

    # carry = 0
    # for i in range(min_length - 1, -1, -1):
    #     temp_sum = (array_one[i] + array_two[i]) + carry

    #     temp_sum = temp_sum % 10
    #     carry = temp_sum // 10

    #     res.append(temp_sum)
    
    # # if carry > 0:
    #     # res.append(carry
    
    # # i = 0
    # # n = len(res) 
    # print(res)


a = LinkedList(6)
b = LinkedList(2)
c = LinkedList(3)

d = LinkedList(4)
e = LinkedList(5)
f = LinkedList(6)

a.next = b
b.next = c
c.next = None

d.next = e
e.next = f
f.next = None

sumOfLinkedLists(a, d)