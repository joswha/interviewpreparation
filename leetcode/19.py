# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = second = head
        length = 0
        
        while first:
            length += 1
            first = first.next
        
        if length == 1:
            return None
        
        # if specific node is exactly the head
        if length - n == 0:
            return head.next
        
        # isolate the redundant node
        index = length - n
        for i in range(index - 1):
            second = second.next
            
        second.next = second.next.next
        return head