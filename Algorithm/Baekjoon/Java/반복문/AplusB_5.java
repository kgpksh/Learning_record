package Algorithm.Baekjoon.Java.반복문;

import java.io.*;

public class AplusB_5 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            String[] arr = br.readLine().split(" ");
            int a = Integer.parseInt(arr[0]);
            int b = Integer.parseInt(arr[1]);

            if (!(a == 0 && b == 0)) {
                bw.write(a + b + "\n");
            } else {
                break;
            }

        }
        br.close();
        bw.flush();
        bw.close();
    }
}
