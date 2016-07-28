import java.util.*;

/****
Graph implemented using Adjacency List
**/

public class Graph
{
	public ArrayList<Vertex> vertices = new ArrayList<Vertex>();

		
	public void addVertex(char label)
	{ vertices.add(new Vertex(label)); }

	public Vertex getVertex(char label)
	{
		for(int i = 0; i < vertices.size(); i++)
		{ 
			if(vertices.get(i).label == label)
				return vertices.get(i);
		}
		return null;
	}

	public void addEdge(char vertexFrom, char vertexTo)
	{ getVertex(vertexFrom).addNeighbor(vertexTo); }

	/* Displays the graph in adjacency list form */
	public void display()
	{
		for(int i = 0; i < vertices.size(); i++)
		{
			System.out.print(vertices.get(i).label + ": ");
			
			for(int j = 0; j < vertices.get(i).neighbors.size(); j++)
				System.out.print("->" + vertices.get(i).neighbors.get(j));
			
			System.out.println();
		}
	}

	/*
		Prints graph through breadth first traversal
	*/
	public void bfs()
	{
		LinkedList<Character> queue = new LinkedList<Character>();
		boolean[] visited = new boolean[vertices.size()];

		char current = vertices.get(0).label;
		queue.add(current);
		visited[0] = true;

		while(!queue.isEmpty())
		{
			current = queue.remove();
			Vertex curV = getVertex(current);

			//add all unvisited neighbors to queue
			for(int i = 0; i < curV.neighbors.size(); i++)
			{
				Vertex neighbor = getVertex(curV.neighbors.get(i));
				if(visited[vertices.indexOf(neighbor)] == false)
				{
					queue.add(neighbor.label);
					visited[vertices.indexOf(neighbor)] = true;
				}
			}
			System.out.print(current + " ");
		}

		System.out.println();
	}

	/*
		Prints graph through depth first traversal
	*/
	public void dfs()
	{
		Stack<Character> stack = new Stack<Character>();
		boolean[] visited = new boolean[vertices.size()];

		stack.push(vertices.get(0).label);
		visited[0] = true;

		while(!stack.empty())
		{
			char current = stack.pop();
			Vertex curV = getVertex(current);

			//add all unvistited neighbors to stack 
			for(int i = 0; i < curV.neighbors.size(); i++)
			{
				Vertex neighbor = getVertex(curV.neighbors.get(i));
				if(visited[vertices.indexOf(neighbor)] == false)
				{
					stack.push(neighbor.label);
					visited[vertices.indexOf(neighbor)] = true;
				}
			}
			System.out.print(current + " ");
		}	
		System.out.println();
	}
}