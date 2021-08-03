# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList

    while current is not None:
        nextNode = current.next
        # although there are 2 whiles, we only access each element once.
        while nextNode and nextNode.value == current.value:
            nextNode = nextNode.next

        current.next = nextNode
        current = nextNode

    return linkedList