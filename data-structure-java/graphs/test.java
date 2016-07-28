public class test
{
	public static void main(String args[])
	{
		Graph g = new Graph();
		
		g.addVertex('A');
		g.addVertex('B');
		g.addVertex('C');
		g.addVertex('D');
		g.addVertex('E');
		g.addVertex('F');

		g.addEdge('A', 'B');
		g.addEdge('A', 'D');
		g.addEdge('A', 'C');

		g.addEdge('B', 'A');
		g.addEdge('B', 'C');
		g.addEdge('B', 'E');

		g.addEdge('C', 'A');
		g.addEdge('C', 'B');

		g.addEdge('D', 'A');
		g.addEdge('D', 'E');
		g.addEdge('D', 'F');

		g.addEdge('E', 'B');
		g.addEdge('E', 'D');

		g.addEdge('F', 'D');


		g.display();
		g.bfs();
	}
}