class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #adds new node to beginning of list
    def insert(self, data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            node.next = self.head
            self.head.prev = node
            self.head = node

    #adds new node to end of list
    def append(self, data):
        if(self.head == None):
            self.insert(data)
        else:
            node = Node(data)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
    #removes node from beginning of list
    def delete(self):
        if(self.head == None):
            return
        else:
            self.head = self.head.next
            if(self.head != None):
                self.head.prev = None

    #removes node from end of list
    def pop(self):
        if(self.head == None):
            return
        else:
            self.tail = self.tail.prev
            if(self.tail != None):
                self.tail.next = None
            
    
    def display(self):
        cur = self.head
        while(cur != None):
            print(cur.data , end=" ")
            cur = cur.next
        print("")

    def displayBackward(self):
        cur = self.tail
        while(cur != None):
            print(cur.data , end=" ")
            cur = cur.prev
        print("")

