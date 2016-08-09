package dataStructures;

import java.lang.Integer;

public class minHeap {
	
	int size;
	int maxSize;
	int[] heap;
	
	public minHeap(int mSize)
	{
		size = 0;
		maxSize = mSize;
		heap = new int[maxSize];
	}
	
	public void insert(int n)
	{
		if(size != maxSize)
			heap[size] = n;
		size++;
		//put newly inserted node in right position in heap
		percUp(size-1);
	}
	
	public int popMin()
	{
		int min = getMin();
		heap[0] = heap[size-1];
		size--;
		percDown(0);
		return min;
	}
	
	public void percUp(int pos)
	{
		while(pos != 0 && heap[(pos-1) / 2] > heap[pos])
		{
			int tmp = heap[(pos-1)/2];
			heap[(pos-1)/2] = heap[pos];
			heap[pos] = tmp;
			pos = (pos-1)/2;
		}
	}
	
	public void percDown(int pos)
	{
		while(pos*2+1 < size)
		{
			int minC = getMinChild(pos);
			if(heap[pos] > heap[minC])
			{
				int tmp = heap[pos];
				heap[pos] = heap[minC];
				heap[minC] = tmp;
			}
			pos = minC;
		}
	}
	
	public int getMin()
	{ return heap[0]; }
	
	//returns index of minChild of given node position
	private Integer getMinChild(int pos)
	{
		if(pos*2+1 > size)
			return null;
		
		int left = pos*2+1;
		int right = pos*2+2;
		
		if(heap[left] <= heap[right])
			return left;
		else
			return right;
	}
	
	public void display()
	{
		for(int i = 0; i < size; i++)
			System.out.print(heap[i] + " ");
		System.out.println();
	}
	
}
