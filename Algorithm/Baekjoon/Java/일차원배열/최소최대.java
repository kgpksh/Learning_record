package Algorithm.Baekjoon.Java.일차원배열;

import java.io.*;

public class 최소최대 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String num = br.readLine();
        int a = Integer.parseInt(num);

        String[] arr = br.readLine().split(" ");

        int min = Integer.parseInt(arr[0]);
        int max = Integer.parseInt(arr[0]);

        for (int i = 1; i < a; i++) {
            int pick = Integer.parseInt(arr[i]);
            if (pick < min) {
                min = pick;
            }
            if (pick > max) {
                max = pick;
            }
        }
        bw.write(min + " " + max);

        br.close();
        bw.flush();
        bw.close();
    }
}
