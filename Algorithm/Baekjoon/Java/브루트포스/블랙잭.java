package Algorithm.Baekjoon.Java.브루트포스;

import java.util.*;

public class 블랙잭 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] range = sc.nextLine().split(" ");
        String[] cards = sc.nextLine().split(" ");
        sc.close();

        int n = Integer.parseInt(range[0]);
        int m = Integer.parseInt(range[1]);
        int maximum = 0;

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int h = j + 1; h < n; h++) {
                    int sum = Integer.parseInt(cards[i]) + Integer.parseInt(cards[j]) +
                            Integer.parseInt(cards[h]);
                    if (sum <= m) {
                        if (m - sum < m - maximum) {
                            maximum = sum;
                        }
                    }

                }
            }
        }

        System.out.println(maximum);
    }
}
