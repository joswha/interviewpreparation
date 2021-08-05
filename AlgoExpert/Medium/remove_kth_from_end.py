# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    i = 1
    curr_kth = head
    next_to_kth = head
    
    while i <= k:
        next_to_kth = next_to_kth.next
        i += 1
    
    if next_to_kth is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    
    while next_to_kth.next is not None:
        next_to_kth = next_to_kth.next
        curr_kth = curr_kth.next
    
    curr_kth.next = curr_kth.next.next
