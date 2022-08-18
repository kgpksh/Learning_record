package Algorithm.Baekjoon.Java.반복문;

import java.util.*;

public class 합 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        System.out.println(num * (1 + num) / 2);

        sc.close();
    }
}
