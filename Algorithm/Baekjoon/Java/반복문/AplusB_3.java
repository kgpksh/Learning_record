package Algorithm.Baekjoon.Java.반복문;

import java.util.*;

public class AplusB_3 {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        for (int i = 0; i < num; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println(a + b);
        }

        sc.close();
    }
}
