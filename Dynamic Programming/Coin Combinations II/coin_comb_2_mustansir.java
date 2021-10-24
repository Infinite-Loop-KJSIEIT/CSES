
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
	    int mod=1e9;
	    int[] c = new int[n];
	    for(int i =0;i<n;i++)
	    {
	       c[i]=Integer.parseInt(cia[i]); 
	    }
	    int dp[][] = new int[n+1][target+1];
		dp[0][0] = 1;
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j <= target; j++) {
      dp[i][j] = dp[i-1][j];
      int left = j-x[i-1];
      if (left >= 0) {
	(dp[i][j] += dp[i][left]) %= mod;
      }
    }
  }
  
        System.out.println(dp[target]); 
	}
}
