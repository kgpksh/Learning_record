package Algorithm.Baekjoon.Java.기본_수학_2;

import java.util.*;

public class 소수 {
    private static boolean is_prime(int n) {
        if (n == 1) {
            return false;
        }
        for (int i = 2; i < (int) Math.sqrt(n) + 1; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        sc.close();

        int sum = 0;
        int min = 10001;
        for (int i = m; i <= n; i++) {
            if (is_prime(i)) {
                sum += i;
                min = Math.min(i, min);
            }
        }

        if (min == 10001) {
            System.out.println(-1);
        } else {
            System.out.println(sum);
            System.out.println(min);
        }
    }
}
