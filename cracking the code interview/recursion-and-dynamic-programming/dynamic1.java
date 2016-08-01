/*
*Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
*steps at a time. Implement a method to count how many possible ways the child can run up the
*stairs.
*
* Solution: Dynamic programming, to solve for n first solve for n-1, to solve for
* n-1 first solve for n-2, etc etc.
*
* Many of the recursive calls will perform the same calculations making the runtime
* roughly O(3^n) where n is the number of steps in the staircase.
*
* To improve on this implement the algorithm with some sort of cache so that instead
* of repeating calculations just look up the answer if it was already solved. This
* way you will only perform calculations on new problems only. 
*/

package tests;

import java.util.*;

public class dynamic1 {
	
	public static int countStepPerm(int n)
	{
		//set up the cache
		int[] cache = new int[n+1];
		Arrays.fill(cache, -1);
		
		return countStepPerm(n, cache);
	}
	
	public static int countStepPerm(int n, int[] cache)
	{
		//base case, if we reached this then 
		//this is a valid permutation
		if(n == 0)
			return 1;
		else if(n < 0) //not valid permutation
			return 0;
		else if(cache[n] > -1) //we already found answer so just look up in cache
			return cache[n];
		//answer has not been found for this one so calculate and store in cache
		//for future
		else
		{
			cache[n] = countStepPerm(n-1, cache) + 
					   countStepPerm(n-2, cache) + 
					   countStepPerm(n-3, cache);
			return cache[n];
		}
		
		
	}
	
	public static void main(String args[])
	{
		System.out.println(countStepPerm(50));
	}
	
}
