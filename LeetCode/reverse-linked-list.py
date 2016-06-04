# Reverse a singly linked list.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        headC = None
        cur = head
        while(cur != None):
            temp = ListNode(cur.val)
            temp.next = headC
            headC = temp
            cur = cur.next
        
        return headC