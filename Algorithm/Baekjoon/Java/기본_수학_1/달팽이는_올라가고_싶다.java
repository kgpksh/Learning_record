package Algorithm.Baekjoon.Java.기본_수학_1;

import java.io.*;

public class 달팽이는_올라가고_싶다 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] str = br.readLine().split(" ");

        int a = Integer.parseInt(str[0]);
        int b = Integer.parseInt(str[1]);
        int v = Integer.parseInt(str[2]);

        int tmp = (v - b) / (a - b);
        int ttmp = (v - b) % (a - b);
        if (ttmp != 0) {
            bw.write(Integer.toString((int) Math.ceil(tmp) + 1));
        } else {
            bw.write(Integer.toString((int) Math.ceil(tmp)));
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
