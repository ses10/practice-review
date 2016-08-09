import java.*;
import java.lang.String;
import java.util.HashSet;

public class FoxAndWord
{
	public int howManyPairs(String[] words)
    {
        int count = 0;
        for(int i = 0; i < words.length-1; i++)
        {
            int midp = 0;
        	HashSet<String> interestWords = new HashSet<String>();
            while(midp < words[i].length()-1)
            {
            	String cur = words[i].substring(midp+1, words[i].length()) + words[i].substring(0, midp+1);
                for(int j = i+1; j < words.length; j++)
                {
                    if(interestWords.contains(cur))
                        break;
                	if(cur.equals(words[j]))
                    {   
                        count++;
                        interestWords.add(cur);
                    }
                }
                midp++;
            }
        }
        return count;
    }
}