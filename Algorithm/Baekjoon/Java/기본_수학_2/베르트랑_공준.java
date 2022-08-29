package Algorithm.Baekjoon.Java.기본_수학_2;

import java.util.*;

public class 베르트랑_공준 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int n = sc.nextInt();
            if (n == 0) {
                break;
            }

            boolean[] b = new boolean[2 * n + 1];
            for (int i = 0; i < 2 * n + 1; i++) {
                b[i] = true;
            }
            b[0] = false;
            b[1] = false;

            for (int i = 2; i < (int) Math.sqrt(2 * n) + 1; i++) {
                if (b[i]) {
                    int j = 2;
                    while (i * j <= 2 * n) {
                        b[i * j] = false;
                        j++;
                    }
                }
            }

            int answer = 0;
            for (int i = n + 1; i <= 2 * n; i++) {
                if (b[i]) {
                    answer++;
                }
            }
            System.out.println(answer);
        }

        sc.close();
    }
}
