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


}