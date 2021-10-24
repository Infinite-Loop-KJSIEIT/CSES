import java.util.*;
import java.io.*;

public class Main
{
	public static void main(String[] args)throws IOException {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    String xn[]=br.readLine().split(" ");
	    int n = Integer.parseInt(xn[0]);
	    
	    int mod=1e9;
	
	    int dp[]=new int[n+1];
	    dp[0] = 0;
        for (int i = 0; i <= n; i++) {
            for (char c : Integer.toString(i)) {
              dp[i] = Math.min(dp[i], dp[i-(c-'0')]+1);
            }
        }
        System.out.println(dp[n]); 
	}
}
