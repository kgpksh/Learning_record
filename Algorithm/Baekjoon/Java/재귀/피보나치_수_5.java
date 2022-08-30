package Algorithm.Baekjoon.Java.재귀;

import java.util.*;

public class 피보나치_수_5 {
    static int p(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }
        return p(n - 2) + p(n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(p(n));
        sc.close();
    }
}
