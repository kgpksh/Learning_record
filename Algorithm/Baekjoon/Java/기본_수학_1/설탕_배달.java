package Algorithm.Baekjoon.Java.기본_수학_1;

import java.util.Scanner;

public class 설탕_배달 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        if (n % 5 == 0) {
            System.out.println(n / 5);
        } else {
            int p = 0;
            while (n > 0) {
                n -= 3;
                p += 1;
                if (n % 5 == 0) {
                    p += p / 5;
                    System.out.println(n / 5 + p);
                    break;
                } else if (n == 1 || n == 2) {
                    System.out.println(-1);
                    break;
                } else if (n == 0) {
                    System.out.println(p);
                    break;
                }
            }
        }
    }
}
