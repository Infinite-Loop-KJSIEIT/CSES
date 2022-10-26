
import java.io.*;
import java.util.*;

class jass {
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
        int m = nextInt();
        TreeMap<Integer, Integer> concert_map= new TreeMap<>();
        StringBuffer res = new StringBuffer();
        Integer temp;
        Map.Entry<Integer, Integer> val;

        for (int i = 0; i < n; i++) {
            temp = nextInt();
            if (concert_map.containsKey(temp))
                concert_map.put(temp,concert_map.get(temp)+1);
            else concert_map.put(temp,1);
        }
        for (int i = 0; i < m; i++) {
            temp = nextInt();
            val=concert_map.lowerEntry(temp+1);
            if (val!=null){
                res.append(val.getKey()).append('\n');
                if (val.getValue() == 1)
                    concert_map.remove(val.getKey());
                else
                    concert_map.put(val.getKey(),val.getValue()-1);
            }else
                res.append("-1\n");
        }

        System.out.println(res);
        
    }

}
