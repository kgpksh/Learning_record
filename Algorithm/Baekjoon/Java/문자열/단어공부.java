package Algorithm.Baekjoon.Java.문자열;

import java.io.*;

public class 단어공부 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = br.readLine();
        s = s.toUpperCase();
        String[] str = s.split("");
        int[] cnt = new int[26];

        for (String a : str) {
            cnt[a.charAt(0) - 'A']++;
        }

        int max = -1;
        for (int i : cnt) {
            if (i > max) {
                max = i;
            }
        }

        int maxcnt = 0;
        int idx = -1;

        for (int i = 0; i < 26; i++) {
            if (cnt[i] == max) {
                maxcnt++;
                idx = i;
            }
        }

        if (maxcnt > 1) {
            bw.write("?");
        } else {
            bw.write((char) (idx + 'A'));
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
