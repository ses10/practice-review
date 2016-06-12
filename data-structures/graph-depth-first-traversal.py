class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacentTo = {}

    #addAdjacent
    def addAdjacent(self, vertex, weight=0):
        self.adjacentTo[vertex] = weight

    #getAdjacents
        #returns vertices adjacent to this Vertex
        #rtnType: dictionary
    def getAdjacents(self):
        return self.adjacentTo.keys()

    #getWeight
        #returns the weight of this vertex and one of its adjacent
    def getWeight(self, adjVertex):
        return self.adjacentTo[adjVertex]

    #displays all adjacent vertices
    def display(self):
        print(self.id + ": ", end="")
        for key in self.adjacentTo.keys():
            print("->" + key, end="")
        print()
        


class WeightedGraph:
    def __init__(self):
        self.vertices = {}
        self.numVertex = 0

    def addVertex(self, id):
        self.vertices[id] = Vertex(id)
        self.numVertex += 1

    def getVertex(self, id):
        if id in self.vertices:
            return self.vertices[id]
        else:
            return None

    #returns dictionary of vertices
    def getVertices(self):
        return self.vertices.keys()
    
    def addEdge(self,fromVer,toVer, weight = 0):
        if fromVer not in self.vertices:
            addVertex(fromVer)
        if toVer not in self.vertices:
            addVertex(toVer)
        self.vertices[fromVer].addAdjacent(self.vertices[toVer].id, weight)

    def display(self):
        for x in self.vertices:
            vertex = self.getVertex(x)
            vertex.display()

#Prints every vertex in graph through Depth-First traversal
#uses stack
def printDepthFirst(g, Vid):
    visited = [False] * g.numVertex
    stack = []
    stack.insert(0, Vid)
    visited[ord(Vid)-ord('A')] = True

    while len(stack) != 0:
        v = stack.pop()
        print(v, end=" ")
        for i in g.getVertex(v).getAdjacents():
            if not visited[ord(i)-ord('A')]:
                visited[ord(i)-ord('A')] = True
                stack.insert(0, i)
    print()

def main():
    g = WeightedGraph()

    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')

    g.addEdge('A', 'B')
    g.addEdge('A', 'C')
    g.addEdge('A', 'D')

    g.addEdge('B', 'A')
    
    g.addEdge('C', 'A')
    g.addEdge('C', 'E')

    g.addEdge('D', 'A')
    g.addEdge('D', 'E')

    g.addEdge('E', 'C')
    g.addEdge('E', 'D')
    
    printDepthFirst(g, 'A')


main()
