package Algorithm.Baekjoon.Java.일차원배열;

import java.io.*;

public class 최댓값 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int index = 0;
        int count = 0;
        int max = 0;

        for (int i = 0; i < 9; i++) {
            count++;
            String num = br.readLine();
            int a = Integer.parseInt(num);
            if (a > max) {
                index = count;
                max = a;
            }
        }
        bw.write(max + "\n");
        bw.write(index + "\n");

        br.close();
        bw.flush();
        bw.close();
    }
}
