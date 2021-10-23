import java.io.*;
import java.util.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Dice_Combinations {
    static final int IBIG = 1000000007;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int dp[] = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= 6 && i - j >= 0; j++) {
                dp[i] += dp[i - j];
                dp[i] %= IBIG;
            }
        }

        System.out.println(dp[n]);
    }
}
