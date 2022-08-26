package Algorithm.Baekjoon.Java.기본_수학_2;

import java.util.*;

public class 소수_구하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        int m = Integer.parseInt(str[0]);
        int n = Integer.parseInt(str[1]);
        sc.close();

        boolean[] b = new boolean[n + 1];
        for (int i = 0; i < n + 1; i++) {
            b[i] = true;
        }
        b[0] = false;
        b[1] = false;

        for (int i = 2; i < (int) Math.sqrt(n) + 1; i++) {
            if (b[i]) {
                int j = 2;
                while (i * j <= n) {
                    b[i * j] = false;
                    j++;
                }
            }
        }

        for (int i = m; i <= n; i++) {
            if (b[i]) {
                System.out.println(i);
            }
        }
    }
}
