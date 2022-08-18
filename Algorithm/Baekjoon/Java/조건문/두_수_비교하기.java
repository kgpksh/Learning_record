package Algorithm.Baekjoon.Java.조건문;

import java.util.*;

public class 두_수_비교하기 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a, b;
        a = sc.nextInt();
        b = sc.nextInt();

        if (a > b) {
            System.out.println(">");
        } else if (a < b) {
            System.out.println("<");
        } else if (a == b) {
            System.out.println("==");
        }

        sc.close();
    }
}
