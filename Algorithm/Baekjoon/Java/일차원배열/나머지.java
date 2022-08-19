package Algorithm.Baekjoon.Java.일차원배열;

import java.util.*;
import java.io.*;

public class 나머지 {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < 10; i++) {
            set.add(Integer.parseInt(br.readLine()) % 42);
        }

        System.out.println(set.size());

        br.close();
    }
}
