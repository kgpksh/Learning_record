package Algorithm.Baekjoon.Java.일차원배열;

import java.io.*;

public class OX퀴즈 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int size = Integer.parseInt(br.readLine());

        int streak = 0;
        int sum = 0;

        for (int i = 0; i < size; i++) {
            String study = br.readLine();
            for (int j = 0; j < study.length(); j++) {
                if (study.charAt(j) == 'X') {
                    if (streak != 0) {
                        sum += ((1 + streak) * streak) / 2;
                    }
                    streak = 0;
                } else {
                    streak += 1;
                }
            }
            if (streak != 0) {
                sum += ((1 + streak) * streak) / 2;
            }
            streak = 0;
            bw.write(sum + "\n");
            sum = 0;
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
