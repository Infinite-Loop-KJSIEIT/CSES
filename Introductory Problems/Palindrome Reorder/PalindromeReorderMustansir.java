
import java.io.*;
import java.util.*;

class PalindromeReorderMustansir {
    static BufferedReader br;
    static StringTokenizer st;

    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(br.readLine());
        }
        return st.nextToken();
    }

    static long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    public static void main(String args[]) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int t = nextInt();
        while (t-- > 0) {
            input();
        }
        br.close();
    }

    public static void input() throws IOException {
        String S = next();
        char[] s = S.toCharArray();
        int[] a = new int[26];
        for (char c : s) {
            a[c - 'A']++;
        }

        int check = 0;
        for (int i = 0; i < 26; i++) {
            check += (a[i] % 2);
        }

        if (check > 1) {
            System.out.println("NO SOLUTION");
            return;
        }

        String result = "";
        for (int i = 0; i < 26; i++) {
            if ((a[i] % 2) == 0) {
                for (int j = 0; j < a[i] / 2; j++) {
                    result += i + 'A';
                }
            }
        }
        for (int i = 0; i < 26; i++) {
            if (a[i] % 2 == 1) {
                for (int j = 0; j < a[i]; j++)
                    result += i + 'A';
            }
        }
        for (int i = 25; i >= 0; i--) {
            if (!(a[i] % 2 == 1)) {
                for (int j = 0; j < a[i] / 2; j++)
                    result += i + 'A';
            }
        }

        System.out.println(result);
        return;

    }

}
