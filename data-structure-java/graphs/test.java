public class test
{
	public static void main(String args[])
	{
		Graph g = new Graph();
		
		g.addVertex('A');
		g.addVertex('B');
		g.addVertex('C');
		g.addVertex('D');

		g.addEdge('A', 'B');
		g.addEdge('A', 'C');
		g.addEdge('A', 'D');
		g.addEdge('B', 'A');
		g.addEdge('B', 'D');
		g.addEdge('C', 'A');
		g.addEdge('D', 'A');
		g.addEdge('D', 'D');


		g.display();
	}
}