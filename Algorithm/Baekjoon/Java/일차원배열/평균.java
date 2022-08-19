package Algorithm.Baekjoon.Java.일차원배열;

import java.io.*;

public class 평균 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int size = Integer.parseInt(br.readLine());
        String[] study = br.readLine().split(" ");
        int max = 0;
        float sum = 0;
        for (int i = 0; i < size; i++) {
            int point = Integer.parseInt(study[i]);
            if (point > max) {
                max = point;
            }
            sum += point;
        }

        bw.write(sum * 100 / (max * size) + "");
        br.close();
        bw.flush();
        bw.close();
    }

}
