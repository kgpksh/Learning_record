package Algorithm.Baekjoon.Java.기본_수학_2;

import java.util.*;

public class 소수_찾기 {
    private static boolean is_prime(int n) {
        if (n == 1) {
            return false;
        }
        for (int i = 2; i < (int) Math.sqrt(n) + 1; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();
        String[] numbers = sc.nextLine().split(" ");
        sc.close();

        int answer = 0;
        for (String s : numbers) {
            if (is_prime(Integer.parseInt(s))) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}
