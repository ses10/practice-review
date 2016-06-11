### Problem
#Given a binary tree, design an algorithm which creates a linked list of all the nodes at
#each depth (e.g., if you have a tree with depth D,you'll have D linked lists).

### Solution
#For each recusion call you check the size of the array of linked lists and see whether 
#there is already a list for the current tree depth.
#If not then the current node in tree becomes the head node for this depth
#If there is then add the current node to the list for this depth

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class ListNode:
	def __init__(self, data):
		self.data = data
		self.next = None


def displayLinkedList(head):
	cur = head
	while(cur != None):
		print(cur.data, end=" ")
		cur = cur.next

	print()

#Given the root of a binary tree and
#an empty array the function adds a linked list 
#of tree nodes for each level in the tree
def getLvlLists(root, arrayList, lvl=1):
	if root == None:
		return

	if len(arrayList) < lvl:
		#arrayList[len(arrayList)] = ListNode(root.data)
		arrayList.append(ListNode(root.data))
	else:
		#inserting the node in linked list
		head = arrayList[lvl-1] 
		temp = ListNode(root.data)
		temp.next = head
		arrayList[lvl-1] = temp

	getLvlLists(root.left, arrayList, lvl+1)
	getLvlLists(root.right, arrayList, lvl+1)

def dis(root):
	if root == None:
		return

	print(root.data, end=" ")
	dis(root.left)
	dis(root.right)


def main():
	
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(6)

	dis(root)
	print()

	li = []

	getLvlLists(root, li, 1)

	for i in li:
		displayLinkedList(i)
