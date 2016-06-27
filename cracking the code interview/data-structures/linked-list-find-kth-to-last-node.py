#Implement an algorithm to find the kth to last element of a singly linked list.

### Solution
#have 2 pointers and seperate them by k - 1 nodes.
#then move them both through the list at the same pace until the further node p2 is at end
#p1 will be the kth to last node in list

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

#Returns the nth to last node of a given linked list
def nthToLast(head, n):
	if n <= 0:
		return None

	p1 = head
	p2 = head

	#move p2 ahead by n - 1 nodes
	for i in range(1,n):
		if p2 == None:
			return None

		p2 = p2.next

	#now move both pointers until end
	while p2.next != None:
		p1 = p1.next
		p2 = p2.next

	return p1

def main():

	head = Node(4)

	for i in range(6):
		new = Node(i)
		new.next = head
		head = new

	print(nthToLast(head, 4).data)

main()