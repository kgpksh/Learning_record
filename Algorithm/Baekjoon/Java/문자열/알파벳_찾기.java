package Algorithm.Baekjoon.Java.문자열;

import java.io.*;

public class 알파벳_찾기 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] s = br.readLine().split("");

        int[] rec = new int[26];
        for (int i = 0; i < 26; i++) {
            rec[i] = -1;
        }

        for (int i = 0; i < s.length; i++) {
            char c = s[i].charAt(0);
            if (rec[c - 'a'] == -1) {
                rec[c - 'a'] = i;
            }

        }

        for (int i = 0; i < 25; i++) {
            bw.write(String.valueOf(rec[i] + " "));
        }
        bw.write(String.valueOf(rec[25]));

        br.close();
        bw.flush();
        bw.close();
    }
}
