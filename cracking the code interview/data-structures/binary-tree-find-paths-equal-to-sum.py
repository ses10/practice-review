### Problem
#You are given a binary tree in which each node contains a value. 
#Design an algorithm to print all paths which sum to a given value. 
#The path does not need to start or end at the root or a leaf.

### Solution
#We use an array to represent the paths in the tree with each
#index in the array corresponding to the tree's level.
#We ask whether the current node in the tree completes a path whose sum 
#equals to the given sum. So we loop from the current node all the way to the root
#and for each node we add its data to the sum and if at any point during the loop
#the cumulative sum equals the sum give we print out that subpath from the current 
#index in the loop to the current level.

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


#prints out all paths in given binary tree whose sum equals the 
#given sum
def findSum(root, sum, path, lvl):
	if root == None:
		return

	path[lvl] = root.data

	s=0
	for i in range(lvl, -1, -1):
		s += path[i]
		if s == sum:
			printPath(path[i:lvl+1])

	findSum(root.left, sum, path, lvl+1)
	findSum(root.right, sum, path, lvl+1)



#prints given path
def printPath(path):
	for i in path:
		print(i,end=" ")
	print()

#gets height of binary tree
def getHeight(root):
    if (root == None):
        return -1
    else:
        lmax = getHeight(root.left)
        rmax = getHeight(root.right)
        
        if(lmax > rmax):
            return lmax + 1
        else :
            return rmax + 1

def main():

	root = Node(1)

	root.left = Node(0)
	root.left.left = Node(2)
	root.left.right = Node(-4)
	root.left.right.left = Node(6)

	root.right = Node(-1)
	root.right.right = Node(2)
	root.right.left = Node(4)
	root.right.right.right = Node(5)
	root.right.right.left = Node(4)

	height = getHeight(root)
	path = [None] * (height + 1)
	sum = 3
	lvl = 0

	findSum(root, sum, path, lvl)

main()