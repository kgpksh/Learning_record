package Algorithm.Baekjoon.Java.정렬;

import java.io.*;

public class 수_정렬하기_3 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[10001];
        for (int i = 0; i < n; i++) {
            arr[Integer.parseInt(br.readLine())]++;
        }
        for (int j = 1; j < 10001; j++) {
            for (int h = 0; h < arr[j]; h++) {
                bw.write(j + "\n");
            }
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
