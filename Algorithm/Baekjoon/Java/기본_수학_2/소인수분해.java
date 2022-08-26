package Algorithm.Baekjoon.Java.기본_수학_2;

import java.util.*;

public class 소인수분해 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        while (n != 1) {
            for (int i = 2; i <= n; i++) {
                if (n % i == 0) {
                    System.out.println(i);
                    n = n / i;
                    break;
                }
            }
        }
    }
}
