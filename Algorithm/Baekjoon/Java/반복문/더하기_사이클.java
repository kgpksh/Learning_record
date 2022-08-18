package Algorithm.Baekjoon.Java.반복문;

import java.io.*;

public class 더하기_사이클 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = br.readLine();
        int a = Integer.parseInt(input);
        int count = 0;
        int next = a;
        while (true) {
            count += 1;
            int ten = next / 10;
            int one = next % 10;
            next = 10 * one + (ten + one) % 10;
            if (a == next) {
                break;
            }
        }

        System.out.println(count);

        br.close();
        bw.flush();
        bw.close();
    }
}
