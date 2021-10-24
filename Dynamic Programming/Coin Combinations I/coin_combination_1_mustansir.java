
import java.util.*;
import java.io.*;

public class Main
{
	public static void main(String[] args)throws IOException {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    String xn[]=br.readLine().split(" ");
	    int n = Integer.parseInt(xn[0]);
	    int target = Integer.parseInt(xn[1]);
	    String cia[]=br.readLine().split(" ");
	    
	    int[] c = new int[n];
	    for(int i =0;i<n;i++)
	    {
	       c[i]=Integer.parseInt(cia[i]); 
	    }
		dp[0] = 1;
          for (int i = 1; i <= target; i++) {
            for (int j = 0; j < n; j++) {
              if (i-c[j] >= 0) {
        	(dp[i] += dp[i-c[j]]) %= mod;
              }
            }
        }  
        System.out.println(dp[target]); 
	}
}
