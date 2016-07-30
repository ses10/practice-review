
public class test 
{
	
	public static void main(String args[])
	{
		Graph g = new Graph(6);
		
		g.addEdge(0, 1);
		g.addEdge(0, 4);
		g.addEdge(0, 3);
		
		g.addEdge(1, 0);
		
		g.addEdge(2, 3);
		
		g.addEdge(4, 0);
		
		g.addEdge(3, 0);
		g.addEdge(3, 2);

		g.addEdge(2, 5);
		
		g.bfs();
		g.dfs();
	}
}
