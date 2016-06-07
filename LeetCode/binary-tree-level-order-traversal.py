#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, #level by level).
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

    #for each level in binary tree add nodes in empty array and add
    #that array to cumulative array of levels    
        
        levels = []
        height = self.getHeight(root)
        for i in range(1, height + 1):
            nodes = []
            self.getLevel(root, i, nodes)
            levels.append(nodes)
        
        return levels
    
    #get the all the nodes in a given level of binary tree
    def getLevel(self, root, level, nodes):
        if(root == None):
            return
        elif(level == 1):
            nodes.append(root.val)
        elif(level > 1):
            self.getLevel(root.left, level-1, nodes)
            self.getLevel(root.right, level-1, nodes)
    
    
    #gets height of binary tree
    def getHeight(self, root):
        if (root == None):
            return 0
        else:
            lmax = self.getHeight(root.left)
            rmax = self.getHeight(root.right)
            
            if(lmax > rmax):
                return lmax + 1
            else :
                return rmax + 1
            
            