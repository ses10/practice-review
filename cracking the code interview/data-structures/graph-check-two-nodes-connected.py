### Problem
#Given a directed graph, design an algorithm to find out whether there is a route
#between two nodes.

### Solution
#Traverse graph with DFS or BFS and check at each vertex whether we found end vertex
#Using BFS as shown here can also give you the shortest path

#Given 2 vertex ids returns True if a route 
#between them exists, False otherwise
def isConnected(g, strt, end):
    visited = [False] * g.numVertex
    q = []
    q.append(strt)
    visited[ord(strt) - ord('A')] = True

    while len(q) != 0:
        v = q.pop()

        if v == end:
            return True
        else:
            adj = g.getVertex(v).getAdjacents()
            for i in adj:
                if not visited[ord(i) - ord('A')]:
                    visited[ord(i) - ord('A')] = True
                    q.append(i)


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

def main():
    g = WeightedGraph()

    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')

    g.addEdge('A', 'B')
    g.addEdge('B', 'D')
    g.addEdge('C', 'A')

    g.addEdge('A', 'C')
    g.addEdge('B', 'A')
    g.addEdge('C', 'D')

    g.addEdge('E', 'A')

    if(isConnected(g, 'A', 'E')):
        print("connected")
    else:
        print("not connected")

main()
