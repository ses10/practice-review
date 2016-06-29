#Given a list of airline tickets represented by pairs of departure and 
#arrival airports [from, to], reconstruct the itinerary in order. 
#All of the tickets belong to a man who departs from JFK. 
#Thus, the itinerary must begin with JFK.

#Note:
#If there are multiple valid itineraries, you should return the 
#itinerary that has the smallest lexical order when read as a single string. 
#For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
#All airports are represented by three capital letters (IATA code).
#You may assume all tickets form at least one valid itinerary.

#Example 1:
#tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
#Example 2:
#tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
#Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. 
#But it is larger in lexical order.

###Solution
#Create a graph from the tickets where [from] are the vertices and [to] are the neighbors
#For each vertix sort its neighbors in increasing lexographical order
#
#Then do a depth first search traversal adding each visited node to the trip[]

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        trip = []
        g = makeGraph(tickets)
        dfs(g, "JFK", trip, len(tickets) + 1)
        return trip


def makeGraph(tickets):
	g = {}
	
	#create the inital graph
	for F, T in tickets:
		g[F] = g.get(F, []) + [T]

	#sort each vertices's neighbors by increasing lexographical order 
	for V in g:
		g[V].sort()

	return g

def dfs(graph, strt, trip, numTickets):
	#add currently visited vertex
	trip.append(strt)

	#only if we used up all tickets
	if len(trip) == numTickets:
		return True

	if strt in graph:
		neighbrs = graph[strt]
		for v in neighbrs:
			n = neighbrs.pop(0)
			if dfs(graph, n, trip, numTickets):
				return True

			#else backtrack
			neighbrs.append(n)

	trip.pop()
	return False