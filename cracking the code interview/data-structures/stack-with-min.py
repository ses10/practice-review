### Problem
#How would you design a stack which, in addition to push and pop, also has a
#function min which returns the minimum element? Push, pop and min should all
#operate in 0(1) time.

###

class StackWithMin():
	def __init__(self):
		self.stack = []
		self.minStack = []
		self.minStack.append(float('inf'))

	def min(self):
		return self.minStack[0];

	def push(self, n):
		if n <= self.minStack[0]:
			self.minStack.insert(0 , n)

		self.stack.insert(0, n)

	def pop(self):
		if self.stack[0] == self.minStack[0]:
			self.minStack.pop(0)

		return self.stack.pop(0)

def main():

	s = StackWithMin()
	s.push(5)
	s.push(9)
	s.push(2)
	s.push(1)
	s.push(22)

	print(s.min())

	s.pop()
	s.pop()
	print(s.min())

	s.pop()
	s.pop()
	print(s.min())

main()