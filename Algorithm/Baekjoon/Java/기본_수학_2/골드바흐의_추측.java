package Algorithm.Baekjoon.Java.기본_수학_2;

import java.util.*;

public class 골드바흐의_추측 {
    static boolean check(int n) {
        if (n == 1) {
            return false;
        }
        int tmp = (int) Math.sqrt(n) + 1;
        for (int i = 2; i < tmp; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    static int adder(int a, int b) {
        if (check(a) && check(b)) {
            return a;
        }
        return adder(a - 1, b + 1);

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int t = 0; t < tc; t++) {
            int n = sc.nextInt();
            if (check(n / 2)) {
                System.out.println(n / 2 + " " + n / 2);
            } else {
                int tmp = adder(n / 2, n / 2);
                System.out.println(tmp + " " + (n - tmp));
            }
        }

        sc.close();
    }
}
