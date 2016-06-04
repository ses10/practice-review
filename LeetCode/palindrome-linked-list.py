# Given a singly linked list, determine if it is a palindrome.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        #create reversed copy of list
        headC = None
        cur = head
        while(cur != None):
            temp = ListNode(cur.val)
            temp.next = headC
            headC = temp
            cur = cur.next
        
        #check if palindrome
        cur = head
        curC = headC
        while(cur != None):
            if(cur.val != curC.val):
                return False
            cur = cur.next
            curC = curC.next
        
        return True