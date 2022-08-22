package Algorithm.Baekjoon.Java.기본_수학_1;

import java.util.*;

public class 분수찾기 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int init = 1;
        int adder = 1;
        while (n > init) {
            adder += 1;
            init += adder;
        }
        int s = 0;
        int m = 0;
        if (adder % 2 == 0) {
            s = adder - (init - n);
            m = 1 + (init - n);
        } else {
            s = 1 + (init - n);
            m = adder - (init - n);
        }

        System.out.println(Integer.toString(s) + "/" + Integer.toString(m));
    }
}
