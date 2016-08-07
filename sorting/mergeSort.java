
public class mergeSort {
	
	/** Given 2 sorted arrays returns the sorted union **/
	public static int[] merge(int[] left, int[] right)
	{
		
		int[] merged = new int[left.length + right.length];
		//keeps track of indexes in arrays
		int ptr = 0;
		int lptr = 0;
		int rptr = 0;
		
		while(ptr < merged.length)
		{
			//no more elements in left
			if(lptr == left.length)
			{
				merged[ptr] = right[rptr];
				rptr++;
			}
			//no more elements in right
			else if(rptr == right.length)
			{
				merged[ptr] = left[lptr];
				lptr++;
			}
			//beginning of left is smaller than right's beginning
			else if(left[lptr] < right[rptr])
			{
				merged[ptr] = left[lptr];
				lptr++;
			}
			//vice versa of above(right is smaller)
			else
			{
				merged[ptr] = right[rptr];
				rptr++;
			}
			
			ptr++;
		}
		
		return merged;
	}
	
	public static int[] mergeSort(int[] nums)
	{
		//base case
		if(nums.length == 1)
			return nums;
		
		int mid = nums.length / 2;
		
		int[] left = mergeSort(subArray(nums, 0, mid-1));
		int[] right = mergeSort(subArray(nums, mid, nums.length-1));
		
		//merge left & right
		return merge(left, right);
	}
	
	/** returns new subarray of given array and start and end indexes inclusive **/
	public static int[] subArray(int[] arr, int strt, int end)
	{
		int size = (end - strt) + 1;
		int[] nArr = new int[size];
		
		for(int i = 0; i < size; i++)
			nArr[i] = arr[strt+i];
	
		return nArr;
	}
	
	public static void main(String args[])
	{
		int[] n = {7,1,3,6,0};
		
		int[] test = mergeSort(n);
		
		for(int i : test)
		{
			System.out.println(i);
		}
	}
}
