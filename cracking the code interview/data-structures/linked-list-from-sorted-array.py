### Problem
#Given a sorted (increasing order) array with unique integer elements, 
#write an algorithm to create a binary search tree with minimal height

### Solution 
#Recursively 
#Take the middle element in the array and set it as the root
#Do the same for the left substree passing in the left half of array
#Do the same for the right substree passing in the right half of array

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

#given a sorted array of integers(increasing)
#creates a binary search tree and
#returns the root
def makeBST(nums):
	if len(nums) == 0:
		return None

	mid = len(nums) // 2
	root = Node(nums[mid])

	root.left = makeBST(nums[:mid])
	root.right = makeBST(nums[mid+1:])

	return root
