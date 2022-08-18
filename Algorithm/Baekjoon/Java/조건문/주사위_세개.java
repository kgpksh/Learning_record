package Algorithm.Baekjoon.Java.조건문;

import java.util.*;

public class 주사위_세개 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String[] numbers = sc.nextLine().split(" ");
        int a = Integer.parseInt(numbers[0]);
        int b = Integer.parseInt(numbers[1]);
        int c = Integer.parseInt(numbers[2]);

        int[] n = { a, b, c };
        Arrays.sort(n);

        if (a != b && b != c && c != a) {
            System.out.println(100 * n[2]);
        } else if (a == b && b == c && c == a) {
            System.out.println(10000 + 1000 * n[2]);
        } else {
            if (a == b) {
                System.out.println(1000 + 100 * a);
            } else if (b == c) {
                System.out.println(1000 + 100 * b);
            } else if (a == c) {
                System.out.println(1000 + 100 * a);
            }
        }
        sc.close();
    }
}
