### Problem
#Implement a MyQueue class which implements a queue using two stacks.

### Solution
#We have 2 stacks old and new. When we want to enqueue an item, push it to new.
#When we want to dequeue an item first if old is empty then for each item in new pop it
#and push it to old. Now the first item that was enqueued is now at the top of old stack
#and we can pop it. 

class MyQueue():
	def __init__(self):
		self.newStack = []
		self.oldStack = []

	def size(self):
		return len(self.newStack) +  len(self.oldStack)

	def enqueue(self, n):
		self.oldStack.insert(0,n)

	def dequeue(self):
		if self.size() == 0:
			return None

		if len(self.newStack) == 0:
			while len(self.oldStack) != 0:
				self.newStack.insert(0, self.oldStack.pop(0))

		return self.newStack.pop(0)


def main():

	q = MyQueue()

	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)


	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())

main()