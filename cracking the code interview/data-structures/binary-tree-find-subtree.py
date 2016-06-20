### Problem 
#You have two very large binary trees: Tl, with millions of nodes, and T2, with
#hundreds of nodes. Create an algorithm to decideifT2 isa subtree ofTl.
#
#A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree ofn
#is identical to T2. That is, if you cut off the tree at node n, the two trees would be
#identical.

### Solution
#For each node in T1 check if current node equals T2 
#if it does than start checking at those 2 nodes whether the trees are the same


class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def isSubTree(t1, t2):
	if t1 == None:
		return False

	if t1.data == t2.data:
		if sameTree(t1, t2):
			return True

	return isSubTree(t1.left, t2) or isSubTree(t1.right, t2)

def sameTree(t1, t2):
	if t1 == None and t2 == None:
		return True

	if t1 == None or t2 == None:
		return False

	if t1.data != t2.data:
		return False

	return sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)


def main():

# T1:
#				7
#		8		   	  11
#	9			20			21
	t1 = Node(7)
	t1.left = Node(8)
	t1.left.left = Node(9)
	t1.right = Node(11)
	t1.right.right = Node(21)
	t1.right.left = Node(20)

# T2:
#			11
#		20		21
#
	t2 = Node(11)
	t2.left = Node(20)
	t2.right = Node(21)

	if isSubTree(t1, t2):
		print("t2 is a subtree of t1")
	else:
		print("not a subtree")

main()