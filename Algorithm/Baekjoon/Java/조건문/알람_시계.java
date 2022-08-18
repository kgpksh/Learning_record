package Algorithm.Baekjoon.Java.조건문;

import java.util.*;

public class 알람_시계 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int h, m;
        h = sc.nextInt();
        m = sc.nextInt();

        if (m < 45) {
            m += 15;
            if (h < 1) {
                h = 23;
            } else {
                h -= 1;
            }

            System.out.println(h);
            System.out.println(m);

        } else {
            m -= 45;
            System.out.println(h);
            System.out.println(m);
        }

        sc.close();
    }
}
