package Algorithm.Baekjoon.Java.일차원배열;

import java.io.*;

public class 평균은넘겠지 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int tc = Integer.parseInt(br.readLine());

        for (int i = 0; i < tc; i++) {
            String[] scores = br.readLine().split(" ");
            int people = Integer.parseInt(scores[0]);

            float sum = 0f;

            for (int student = 1; student <= people; student++) {
                sum += Float.parseFloat(scores[student]);
            }
            float avg = sum / people;

            int upStudent = 0;
            for (int student = 1; student <= people; student++) {
                if (Float.parseFloat(scores[student]) > avg) {
                    upStudent++;
                }
            }

            float students = Float.parseFloat(scores[0]);
            String result = String.format("%.3f", upStudent * 100 / students);

            bw.write(result + "%\n");

        }
        br.close();
        bw.flush();
        bw.close();
    }
}
