package Algorithm.Baekjoon.Java.문자열;

import java.io.*;

public class 숫자의_합 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        br.readLine();
        String[] s = br.readLine().split("");
        int sum = 0;
        for (String i : s) {
            int n = Integer.parseInt(i);
            sum += n;
        }
        bw.write(String.valueOf(sum));

        br.close();
        bw.flush();
        bw.close();
    }
}
