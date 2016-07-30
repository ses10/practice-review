/*
 * Graph implementation using adjacency lists 
 * 
 * Nodes in graph are labeled by numbers
 */

import java.util.*;
import java.util.LinkedList;
import java.util.Stack;

public class Graph {
	
	ArrayList<Node> nodes = new ArrayList<Node>();
	
	/* Initialize graph with # of nodes starting from 0 to numNode - 1 */
	public Graph(int numNode)
	{
		for(int i = 0; i < numNode; i++)
		{ nodes.add(new Node(i)); }
	}
	
	public void addNode()
	{ nodes.add(new Node(nodes.size())); }
	
	public void addEdge(int n1, int n2)
	{ nodes.get(n1).adjacents.add(nodes.get(n2)); }
	
	public void bfs()
	{
		//queue
		LinkedList<Node> q = new LinkedList<Node>();
		
		//set all nodes to not visited
		for(int i = 0; i < nodes.size(); i++)
		{ nodes.get(i).wasVisited = false; }
		
		//enqueue first node
		Node first = nodes.get(0);
		q.add(first);
		
		while(!q.isEmpty())
		{
			Node cur = q.removeFirst();
			cur.wasVisited = true;
			
			//find adjacents of current node
			for(Node n : cur.adjacents)
			{
				if(!n.wasVisited)
				{
					q.addLast(n);
					n.wasVisited = true;
				}
			}
			System.out.print(cur.label + " ");
		}
		System.out.println();
	}
	
	public void dfs()
	{
		//stack
		Stack<Node> s = new Stack<Node>();
		
		//set all nodes to not visited
		for(int i = 0; i < nodes.size(); i++)
		{ nodes.get(i).wasVisited = false; }
		
		//push first node
		Node first = nodes.get(0);
		s.push(first);		
		
		while(!s.isEmpty())
		{
			Node cur = s.pop();
			cur.wasVisited = true;
			
			//find adjacents of current node
			for(Node n : cur.adjacents)
			{
				if(!n.wasVisited)
				{
					s.push(n);
					n.wasVisited = true;
				}
			}
			System.out.print(cur.label + " ");
		}
		System.out.println();		
	}
	
	private class Node
	{
		int label;
		boolean wasVisited;
		LinkedList<Node> adjacents;
		
		public Node(int n)
		{ 
			label = n; 
			wasVisited = false;
			adjacents = new LinkedList<Node>();
		}
	}
	
}
