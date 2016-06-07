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

    def addVertex(self, id):
        self.vertices[id] = Vertex(id)

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
            
