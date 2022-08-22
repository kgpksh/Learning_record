package Algorithm.Baekjoon.Java.기본_수학_1;

import java.io.*;

public class 손익분기점 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] str = br.readLine().split(" ");
        int a = Integer.parseInt(str[0]);
        int b = Integer.parseInt(str[1]);
        int c = Integer.parseInt(str[2]);

        if (b >= c) {
            bw.write(Integer.toString(-1));
        } else {
            double r = Math.ceil((a / (c - b)));

            if (r % 1 == 0) {
                bw.write(Integer.toString((int) r + 1));
            } else {
                bw.write(Integer.toString((int) r));
            }
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
