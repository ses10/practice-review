package sorts;

import dataStructures.*;

public class heapSort {
	
	public static int[] minHeapSort(int [] nums)
	{
		minHeap h = new minHeap(nums.length);
		
		//insert all nums into heap
		for(int i = 0; i < nums.length; i++)
			h.insert(nums[i]);
		
		int[] sortedNums = new int[nums.length];
		
		//keep poping min from heap into new array
		for(int i = 0; i < nums.length; i++)
			sortedNums[i] = h.popMin();
		
		return sortedNums;
	}
	
	public static void main(String args[])
	{
		int[] unsorted = {5,4,3,2,1};
		
		int[] sorted = minHeapSort(unsorted);
		
		for(int i : sorted)
			System.out.println(i);
	}
}
