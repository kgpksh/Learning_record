package Algorithm.Baekjoon.Java.문자열;

import java.util.*;

public class 상수 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String[] twoString = sc.nextLine().split(" ");

        StringBuffer sb1 = new StringBuffer(twoString[0]);
        StringBuffer sb2 = new StringBuffer(twoString[1]);
        int a = Integer.parseInt(sb1.reverse().toString());
        int b = Integer.parseInt(sb2.reverse().toString());
        if (a > b) {
            System.out.println(a);
        } else {
            System.out.println(b);
        }

        sc.close();
    }
}