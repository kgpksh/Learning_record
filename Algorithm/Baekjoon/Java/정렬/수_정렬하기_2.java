package Algorithm.Baekjoon.Java.정렬;

import java.io.*;
import java.util.Arrays;

public class 수_정렬하기_2 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        for (int answer : arr) {
            bw.write(answer + "\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
