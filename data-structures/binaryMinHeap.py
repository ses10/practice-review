class binaryMinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    def buildHeap(self, aList):
        #start at midpoint of heap
        i = len(aList) // 2
        self.size = len(aList)
        self.heap = [0] + aList[:]
        #percolate down all items above midpoint
        while(i > 0):
            self.percDown(i)
            i -= 1

    #insert
    #inserting an item into the heap requires that you add it to
    #the end of the heap and then percolate it up to its proper position 
    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        self.percUp(self.size)

    #given the index of item in heap, function will
    #percolate up to proper position
    def percUp(self, pos):
        while (pos // 2 > 0):
            #if item less than parent
            if(self.heap[pos] < self.heap[pos // 2]):
                #swap
                temp = self.heap[pos // 2]
                self.heap[pos // 2] = self.heap[pos]
                self.heap[pos] = temp
            pos = pos // 2
        
    def delMin(self):
        #store root
        minItem = self.heap[1]
        #move last item to root
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        #percolate new root down to proper position
        self.percDown(1)
        return minItem

    #given the index of item in heap, function will
    #percolate down to proper position
    def percDown(self, pos):
        #make sure we stay in bounds of heap
        while((pos * 2) <= self.size):
            #get the min child of current item
            minChild = self.minChild(pos)
            #swap if parent greater the minChild
            if(self.heap[pos] > self.heap[minChild]):
                temp = self.heap[pos]
                self.heap[pos] = self.heap[minChild]
                self.heap[minChild] = temp

            #point to where we swapped
            pos = minChild
            
    
    #given position of item in heap
    #return position of the min of the 2 children
    def minChild(self, pos):
        #if the last item in the heap is a left child
            #then just return left child since there can't be a right
        if(pos * 2 + 1 > self.size):
            return pos * 2
        else:
            #return left child if smaller
            if(self.heap[pos * 2] < self.heap[pos * 2 + 1]):
                return pos * 2
            #return right child
            else:
                return pos * 2 + 1

    def display(self):
        print (self.heap[1:])
    

