#Implmenation of Trie using keys containing only the lowercase alphabet

class Node:
	def __init__(self):
		self.children = [None] * 26
		self.isLeaf = False
		self.data = None


class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, key, value):
		cur = self.root

		for char in key:
			index = ord(char) - ord('a')
			if cur.children[index] == None:
				cur.children[index] = Node()
			
			cur = cur.children[index]

		cur.isLeaf = True
		cur.data = value

	#given a key return the value associated 
	#if not found return None
	def find(self, key):
		cur = self.root

		for char in key:
			index = ord(char) - ord('a')
			if cur.children[index] == None:
				return None

			cur = cur.children[index]

		if cur.isLeaf:
			return cur.data
		else:
			return None

	#given a string returns True if string is a key in trie
	#False other wise
	def isKey(self, key):
		if self.find(key) != None:
			return True
		else:
			return False

def main():

	t = Trie()
	t.insert('amy', 10)
	t.insert('oscar', 20)
	t.insert('max', 30)
	t.insert('mom', 40)

	print(t.find('oscar'))
	print(t.find('bob'))

	if t.isKey('amy'):
		print('amy is a key')
	else:
		print('amy is not a key')

main()