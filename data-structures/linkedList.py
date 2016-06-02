class Node:
    def __init__(self, data):
        self.__next = None
        self.__data = data

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getNext(self):
        return self.__next

    def setNext(self, node):
        self.__next = node

class LinkedList:
    def __init__(self):
        self.__head = None

    def getHead(self):
        return self.__head

    #insert
    #adds node to the beginning of the list
    def add(self, data):
        if(self.__head != None):
            node = Node(data)
            node.setNext(self.__head)
            self.__head = node
        else:
            self.__head = Node(data)
            

    #delete
    #removes node from beginning of list
    def remove(self):
        if(self.__head != None):
            self.__head = self.__head.getNext()
                

    #find
    #returns whether Node is in list
    def find(self, data):
        if(self.__head != None):
            curNode = self.__head
            while(curNode != None):
                if(curNode.getData() == data):
                    return True
                else:
                    curNode = curNode.getNext()
        else:
            return False

    def print(self):
        curNode = self.__head
        while(curNode != None):
            print(curNode.getData(), end=" ")
            curNode = curNode.getNext()


