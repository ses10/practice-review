/*** Problem
You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a
method to insert M into N such that M starts at bit j and ends at bit i. You can assume
that the bits j through i have enough space to fit all of M. That is,if M= 10011,
you can assume that there are at least 5 bits between j and i. You would not, for
example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.
EXAMPLE:
Input: N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100


Solution
There are 3 steps to this
1. Clear the bits j-i in N
2. Left shift M until it lines up with j-i
3. Merge M and N through | (bitwise or) operation

In order to clear the j-i bits you need a mask with all 1s except between
bits j-i. Then finally clear the j-i bits by N & mask (bitwise and)operation.
**/



public class bitManip1
{
	public static void main(String args[])
	{
		System.out.println(updateBits(12, 83, 2, 5));
	}

	public static int updateBits(int m, int n, int i, int j)
	{	

		//start creating the mask to clear bits j-i
		int ones = ~0;
		int left = ones << j + 1;
		int right = (1 << i) - 1;

		int mask = left | right;

		//now that we have the mask we can clear bits j-i
		int nClr = n & mask;

		//shift m to line up 
		int mShift = m << i;

		return nClr | mShift;
	}
}