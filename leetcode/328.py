class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList(head):
    odd = head
    even = head.next

    cpy_odd = odd
    cpy_even = even

    

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

oddEvenList(n1)