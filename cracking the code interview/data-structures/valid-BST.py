#Implement a function to check if a binary tree is a binary search tree.

### Solution
#Since a binary search tree is ordered from left to right in increasing order
#we can traverse the tree inorder and keep track of the last node passed
#we make sure that each node value greater than the last
#
#runtime O(n) because we visit each node it in tree
#space   O(n)

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


#given the root node of a binary tree
#returns True if root is a binary search tree
def isBST(root):
	lastNode = Node(float('-inf'))
	return checkBST(root, lastNode)

def checkBST(root, lastNode):
	if root == None:
		return True

	if not checkBST(root.left, lastNode):
		return False

	if root.val <= lastNode.val:
		return False
	lastNode.val = root.val

	if not checkBST(root.right, lastNode):
		return False

	return True

def main():
	root = Node(5)
	root.left = Node(3)
	root.left.right = Node(5)
	root.right = Node(7)

	if isBST(root):
		print("is bst")
	else:
		print("not bst")
main()