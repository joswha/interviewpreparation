class Node(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    target_dict = []
    if head is None:
        return False
    
    curr = head.next
    while curr:
        if curr not in target_dict:
            target_dict.append(curr)
            curr = curr.next
        else:
            return True
    return False
    # if head is None:
    #     return False
    # curr = head.next
    # fast = curr.next
    # while curr:
    #     if curr == fast:
    #         return True
    #     print(curr.value, fast.value)
    #     curr = curr.next
    #     fast = curr.next
    # else:
    #     return False

n1 = Node(3)
n2 = Node(2)
n3 = Node(0)
n4 = Node(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

print(hasCycle(n1))
