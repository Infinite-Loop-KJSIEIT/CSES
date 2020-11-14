import java.io.*;
import java.util.*;
 
public class GridPathsVedantKokate {
	static boolean[][] v = new boolean[9][9];
	static char[] s;
	static int ans=0;
	static void solve(int i, int j, int n) {
		//System.out.println(i+" "+j+" "+n);
		if (i == 7 && j == 1) {
			if (n == 48)
				ans++;
			return;
		}
		
		boolean u = v[i - 1][j];
		boolean d = v[i + 1][j];
		boolean l = v[i][j - 1];
		boolean r = v[i][j + 1];
		if ((u && d && !l && !r) || (!u && !d && l && r)||n==48)
			return ;
		v[i][j] = true;	
		char p=s[n]	;
		
		if (!u && (p == 'U' || p == '?'))
			solve(i - 1, j, n+1);
		if (!d && (p == 'D' || p == '?'))
			solve(i + 1, j, n+1);
		if (!l && (p == 'L' || p == '?'))
			solve(i, j - 1, n+1);
		if (!r && (p == 'R' || p == '?'))
			solve(i, j + 1, n+1);
		v[i][j] = false;
		
	}
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner (System.in);
		s=sc.nextLine().toCharArray();
		for(int i=0;i<9;i++){
			v[i][0]=true;v[i][8]=true;
			v[0][i]=true;v[8][i]=true;
		}
		solve(1, 1, 0);
		System.out.println(ans);
	}
}
