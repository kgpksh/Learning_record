package Algorithm.Baekjoon.Java.정렬;

import java.io.*;
import java.util.*;

public class 커트라인 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);

        String[] scores = br.readLine().split(" ");

        Integer[] points = new Integer[n];

        for (int i = 0; i < n; i++) {
            points[i] = Integer.parseInt(scores[i]);
        }

        Arrays.sort(points, Collections.reverseOrder());

        bw.write(points[k - 1] + "");

        br.close();
        bw.flush();
        bw.close();
    }
}