package Algorithm.Baekjoon.Java.함수;

import java.util.*;

public class 셀프_넘버 {
    private static int sn(int n) {
        char[] c = Integer.toString(n).toCharArray();
        for (int i = 0; i < c.length; i++) {
            n += Character.getNumericValue(c[i]);
        }
        return n;
    }

    public static void main(String args[]) {
        HashSet<Integer> comparer = new HashSet<Integer>();
        HashSet<Integer> ten_thousand = new HashSet<Integer>();

        for (int i = 1; i < 10001; i++) {
            comparer.add(sn(i));
        }

        for (int i = 1; i < 10001; i++) {
            ten_thousand.add(i);
        }

        ten_thousand.removeAll(comparer);

        for (int i : ten_thousand) {
            System.out.println(i);
        }
    }
}
