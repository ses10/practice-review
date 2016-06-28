/*** 
Problem
Given a real number between 0 and 1(e.g., 0.72)that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary
with at most 32 characters, print "ERROR."


***/

public class bitManip2
{
	public static void main(String args[])
	{
		
		System.out.println(decimalBinary(.550));
	}

	/***
	Given a double n, where 0 <= n <= 1
	returns a string of the binary fractional part of n
	***/
	public static String decimalBinary(double n)
	{
		if (!(n >= 0 && n <= 1))
			return "ERROR";

		StringBuilder dec = new StringBuilder(".");

		while(n > 0 && dec.length() <= 32)
		{
			n *= 2;
			if(n >= 1)
			{
				dec.append(1);
				n -= 1;
			}
			else
				dec.append(0);
		}

		return dec.toString();
	}
}