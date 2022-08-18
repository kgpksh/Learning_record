package Algorithm.Baekjoon.Java.반복문;

import java.io.*;

public class 빠른AplusB {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int num = Integer.parseInt(br.readLine());
        for (int i = 0; i < num; i++) {
            String[] str = br.readLine().split(" ");
            int a = Integer.parseInt(str[0]);
            int b = Integer.parseInt(str[1]);
            bw.write(a + b + "\n");
        }
        bw.flush();
    }
}
