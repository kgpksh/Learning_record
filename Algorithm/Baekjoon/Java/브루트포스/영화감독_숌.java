package Algorithm.Baekjoon.Java.브루트포스;

import java.util.*;

public class 영화감독_숌 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        sc.close();

        int cnt = 1;
        int init = 666;

        while (true) {
            if (cnt == n) {
                System.out.println(init);
                break;
            }

            init++;
            if (Integer.toString(init).contains("666")) {
                cnt++;
            }
        }
    }
}
