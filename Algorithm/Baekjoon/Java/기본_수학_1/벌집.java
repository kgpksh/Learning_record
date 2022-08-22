package Algorithm.Baekjoon.Java.기본_수학_1;

import java.util.Scanner;

public class 벌집 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int a = 1;
        int b = 1;
        while (a < n) {
            a = a + (b * 6);
            b++;
        }
        System.out.println(b);
    }
}
