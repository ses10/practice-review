### Problem
#Write an algorithm to find the 'next'node (i.e., in-order successor) of a given node in
#a binary search tree. You may assume that each nodehas a link to its parent.

### Solution
#Because this a BST the inorder successor of a given node n is always in the right subtree.
#If n has a right child then the inorder successor is the left most node in the right subtree.
#If n does not have a right child then we keep going up the tree until the current node is a left 
#child of the current parent and the inorder successor is the parent
#
#Runtime: average case - O(log n ), worse case - O(n)

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def getInorderSuccessor(node):
	if node == None:
		return None

	if node.right != None:
		return leftMostChild(node.right)
	else:
		cur = node
		parent = cur.parent
		
		while cur != parent.left:
			cur = parent
			parent = parent.parent
			
			#we have reached root which means the node given in the initial 
			#call was the last node in tree
			if parent == None:
				return None

		return parent


def leftMostChild(node):
	if node == None:
		return None

	if node.left == None:
		return node
	else:
		return leftMostChild(node.left)


def main():
#BST: 
#                 7
#              5     12
#           
#
#
	root = Node(7)

	root.left = Node(5)
	root.left.parent = root
	root.right = Node(12)
	root.right.parent = root


	print(getInorderSuccessor(root.right))

	print("hello")

main()