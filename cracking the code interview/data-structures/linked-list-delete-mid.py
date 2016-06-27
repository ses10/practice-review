### Problem
#Implement an algorithm to delete a node in the middle of a singly linked list, given
#only access to that node.

### Solution 
#Just copy the value of the next node to the current node.
#Then delete next node
# O(1) runtime

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None


#Given a node that is in the middle of a linked list
#deletes that node and returns True if successful 
#False otherwise
def delMid(node):
	if node == None or node.next == None:
		return False

	node.data = node.next.data
	node.next = node.next.next
