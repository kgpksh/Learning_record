package Algorithm.Baekjoon.Java.반복문;

import java.io.*;

public class X보다_작은_수 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] standard = br.readLine().split(" ");
        int num = Integer.parseInt(standard[0]);
        int std = Integer.parseInt(standard[1]);

        String[] arr = br.readLine().split(" ");

        for (int i = 0; i < num; i++) {
            int answer = Integer.parseInt(arr[i]);
            if (answer < std) {
                bw.write(answer + " ");
            }
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
