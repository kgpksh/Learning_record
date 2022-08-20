package Algorithm.Baekjoon.Java.문자열;

import java.io.*;

public class 문자열_반복 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int cas = Integer.parseInt(br.readLine());

        for (int i = 0; i < cas; i++) {
            String[] s = br.readLine().split(" ");
            int n = Integer.parseInt(s[0]);
            for (int j = 0; j < s[1].length(); j++) {
                for (int k = 0; k < n; k++) {
                    bw.write(s[1].charAt(j));
                }
            }
            if (!(i == cas - 1)) {
                bw.write("\n");
            }
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
