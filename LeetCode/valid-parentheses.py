#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine 
#if the input string is valid.
#
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" 
#and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a1 = ['(', '{', '[']
        a2 = [')', '}', ']']
        stack = []
        
        for char in s:
            if char in a1:
                stack.insert(0,char)
            else:
                if len(stack) != 0 and stack[0] == a1[a2.index(char)]:
                    stack.pop(0)
                else:
                    return False
        
        
        if len(stack) == 0:
            return True
        else:
            return False