package Algorithm.Baekjoon.Java.반복문;

import java.io.*;

public class AplusB_4 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = "";

        while ((input = br.readLine()) != null) {
            String[] arr = input.split(" ");
            int a = Integer.parseInt(arr[0]);
            int b = Integer.parseInt(arr[1]);
            bw.write(a + b + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
