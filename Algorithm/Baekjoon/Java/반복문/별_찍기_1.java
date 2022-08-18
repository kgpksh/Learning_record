package Algorithm.Baekjoon.Java.반복문;

import java.io.*;

public class 별_찍기_1 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int num = Integer.parseInt(br.readLine());

        for (int i = 1; i <= num; i++) {
            StringBuffer star = new StringBuffer();

            for (int j = 1; j <= i; j++) {
                star.append("*");
            }

            bw.write(star + "\n");

        }
        br.close();
        bw.flush();
        bw.close();
    }
}
