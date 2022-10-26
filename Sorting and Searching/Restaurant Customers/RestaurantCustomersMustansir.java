
import java.io.*;
import java.util.*;

class RestaurantCustomerMustansir{
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
        int n = nextInt();
        String[] input;

        Map<Integer, Integer> map = new TreeMap<>();

        while (n-- > 0) {
            input = br.readLine().split(" ");

            map.put(Integer.parseInt(input[0]), 1);
            map.put(Integer.parseInt(input[1]), -1);
        }
        int sum = 0;
        int res = 0;

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            sum += entry.getValue();
            if (res < sum)
                res = sum;
        }

        System.out.println(res);
    }

}
