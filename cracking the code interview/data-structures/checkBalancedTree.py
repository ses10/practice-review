######   Problem   ########
#Implement a function to check if a binary tree is balanced. For the purposes of this
#question, a balanced tree is defined to be a tree such that the heights of the two
#subtrees of any node never differ by more than one.

######   Solution    ########
#Starting at the root, for each subtree get the height and if the difference between 
#the heights are greater 1 than tree is not balanced.
#
#Because at each node you are getting the height and checking if balanced at the same recursion
#the runtime is O(n), space is O(H) where H is height of tree


class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


def isBalanced(root):
	if(getHeight(root) == -1):
		return False
	else: 
		return True

#gets the height of the tree while also checking if it's
#balanced, returns -1 if unbalanced tree
def getHeight(root):
	if root == None:
		return 0

	lHeight = getHeight(root.left)
	rHeight = getHeight(root.right)

	if lHeight == -1 | rHeight == -1:
		return -1

	maxHeight = max(lHeight, rHeight)

	#checking for balance
	if abs(lHeight - rHeight) > 1:
		return -1
	else:	
		return maxHeight + 1

