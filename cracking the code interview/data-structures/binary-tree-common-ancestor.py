### Problem 
#Design an algorithm and write code to find the first common ancestor of two nodes
#in a binary tree. Avoidstoring additional nodes in a data structure.NOTE: This is not
#necessarily a binary search tree.

### Solution
##This assumes we dont have links to parent nodes
#With a single traversal we first find the two given nodes p and q, then pass the findings 
#back up the tree. When going back up the tree each node checks whether their left/right 
#is p and or q and from there the following cases occur.
#
#Case : Both of the nodes children are p or q
#	then this node is the common ancestor & we return it
#
#Case : Only one of the nodes are p/q
#	just return the non-null node
#
#Case : One of the nodes is neither null, p, or q.
#	Then this is the common ancestor found earlier and we just pass it up.


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None	

class Result:
	def __init__(self, n, isAnc):
		self.node = n
		self.isAncestor = isAnc

#given a binary tree and two nodes n1,n2
#returns the common ancestor of n1 and n2
def commonAncestor(root, n1, n2):
	result = commonAncestorHelper(root, n1, n2)

	if result.isAncestor:
		return result.node
	else:
		return None

def commonAncestorHelper(root, n1,n2):
	if root == None:
		return Result(None, False)

	if root == n1 and root == n2:
		return Result(root, True)

	#search for n1 & n2 in children
	resultLeft = commonAncestorHelper(root.left, n1, n2)
	if resultLeft.isAncestor:
		return resultLeft

	resultRight = commonAncestorHelper(root.right, n1, n2)
	if resultRight.isAncestor:
		return resultRight

		#In this case the current root is the ancestor
	if resultLeft.node != None and resultRight.node != None:
		return Result(root, True)

		#if this node is n1 or n2 and one of it's subnodes is
		# n1/n2 then this node is the ancestor
	elif root == n1 or root == n2:
		if resultLeft.node != None or resultRight.node != None:
			isAncestor = True
		else:
			isAncestor = False
		return Result(root, isAncestor)

	else:
		if resultLeft.node != None:
			return Result(resultLeft.node, False)
		else:
			return Result(resultRight.node, False)

def main():
	
	root = Node(3)
	root.left = Node(1)
	root.right = Node(5)

	root.left.right = Node(6)
	root.left.left = Node(7)
	root.left.left.left = Node(11)
	root.left.left.left.left = Node(12)

	root.right.right = Node(8)
	root.right.right.right = Node(33)
	root.right.right.left = Node(20)

	res = commonAncestor(root, root.left.left.left, root.left.right)
	if res != None:
		print("The ancestor is: " + str(res.key))

main()


	


