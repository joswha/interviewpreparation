class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that 
# has Node.val == val, and return the new head.
def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if not head:
        return
    
    temp = ListNode(1)
    temp.next = head

    prev, curr = temp, temp.next
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return temp.next