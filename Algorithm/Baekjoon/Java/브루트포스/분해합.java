package Algorithm.Baekjoon.Java.브루트포스;

import java.util.*;

public class 분해합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            String[] str = Integer.toString(i).split("");
            int tmp = 0;
            for (String s : str) {
                tmp += Integer.parseInt(s);
            }

            if (i + tmp == n) {
                answer = i;
                break;
            }
        }

        System.out.println(answer);
    }
}
