package Algorithm.Baekjoon.Java.반복문;

import java.util.*;

public class 영수증 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int total = Integer.parseInt(sc.nextLine());
        int num = Integer.parseInt(sc.nextLine());

        int comparer = 0;
        for (int i = 0; i < num; i++) {
            String[] tmp = sc.nextLine().split(" ");
            int a = Integer.parseInt(tmp[0]);
            int b = Integer.parseInt(tmp[1]);

            comparer += a * b;
        }

        if (total == comparer) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        sc.close();
    }
}
