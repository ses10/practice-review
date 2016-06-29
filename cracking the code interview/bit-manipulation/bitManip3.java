/***
Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.
***/

class bitManip3
{
	public static void main(String args[])
	{
		System.out.println(getNextInt(22));
		System.out.println(getPrevInt(22));
	}

	/***
	Given a positive integer n, returns the next 
	largest int with the same number of 1s in its binary format as n
	***/
	public static int getNextInt(int n)
	{
		int c = n;
		int cnt1 = 0;
		int cnt0 = 0;

		/** start calculating position of first non trailing zero p **/

		//nontrailing zero means a 1 has to be before a zero.
			//so any zeros at the start need to be accounted for since they are trailing
		while( ((c & 1) == 0) && (c != 0) )
		{
			cnt0++;
			c >>= 1;
		}

		//get the # of 1s before the 1st nontrailing zero p
		while(  (c & 1) == 1 )
		{
			cnt1++;
			c >>= 1;
		}

		//check for cases where there is no longer a number greater than n that
			//has the same number of 1s as n. Or if n is 0
		if( cnt0 + cnt1 == 31 || cnt0 + cnt1 == 0 )
		{ return -1; }

		// p, the first nontrailing zero
		int p = cnt0 + cnt1;

		
		int nxtBiggest =  n | (1 << p); //now set p to 1
		nxtBiggest =  nxtBiggest & ~((1 << p) - 1); // clear bits to right of p
		nxtBiggest = nxtBiggest | (1 << (cnt1 - 1)) - 1; //insert cnt1 - 1 ones to right of p

		return nxtBiggest;
	}

	/***
	Given a positive integer n, returns the next 
	smallest int with the same number of 1s in its binary format as n
	***/
	public static int getPrevInt(int n)
	{
		int c = n;
		int cnt1 = 0;
		int cnt0 = 0;

		/** start calculating position of first non trailing one, p **/

		//nontrailing 1 means a 0 has to be before a zero.
			//so any ones at the start need to be accounted for since they are trailing
		while((c & 1) == 1 )
		{
			cnt1++;
			c >>= 1;
		}

		if(c == 0) return -1;

		//get the # of 0s before the 1st nontrailing one p
		while(((c & 1) == 0) && (c != 0))
		{
			cnt0++;
			c >>= 1;
		}

		// p, the first nontrailing one
		int p = cnt0 + cnt1;

		//set p to 0 and clear the bits to right of p 
		int nxtSmallest = n & ((~0) << p+1);
		int mask = (1 << (cnt1 + 1)) - 1; //the # of 1s + 1, before p
		nxtSmallest = nxtSmallest | (mask << (cnt0 - 1));

		return nxtSmallest;
	}

}