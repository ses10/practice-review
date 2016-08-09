
import java.lang.*;
import java.util.ArrayList;

public class quickSort {
	public static ArrayList<Integer> sort(ArrayList<Integer> nums)
	{
		if(nums.size() <= 1)
			return nums;
		
		int mid = nums.size() / 2;
		ArrayList<Integer> left = new ArrayList<Integer>();
		ArrayList<Integer> right = new ArrayList<Integer>();
		ArrayList<Integer> sorted = new ArrayList<Integer>();
		
		for(int i = 0; i < nums.size(); i++)
		{
			if(i != mid)
			{
				if(nums.get(i) <= nums.get(mid))
					left.add(nums.get(i));
				else
					right.add(nums.get(i));
			}
		}
	
		sorted.addAll(sort(left));
		sorted.add(nums.get(mid));
		sorted.addAll(sort(right));
		
		return sorted;
		
		
	}
	
	public static void main(String args[])
	{
		ArrayList<Integer> a = new ArrayList<Integer>();
		
		a.add(6900);
		a.add(5);
		a.add(41);
		a.add(3);
		a.add(32);
		a.add(4);
		
		a = sort(a);
		
		for(int i : a)
			System.out.println(i);
	}
}
