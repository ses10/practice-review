import java.util.*;

public class Vertex
{
	char label;
	ArrayList<Character> neighbors = new ArrayList<Character>();

	public Vertex(char label)
	{
		this.label = label;
	}

	public void addNeighbor(char vertex)
	{
		neighbors.add(vertex);
	}
}