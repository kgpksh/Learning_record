package Algorithm.Baekjoon.Java.함수;

import java.util.Scanner;

public class 한수 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();

        if (a < 100) {
            System.out.println(a);
        } else {
            int cnt = 99;
            for (int i = 100; i < a + 1; i++) {
                if (i != 1000) {
                    String[] str = Integer.toString(i).split("");
                    if (Integer.parseInt(str[0]) - Integer.parseInt(str[1]) == Integer.parseInt(str[1])
                            - Integer.parseInt(str[2])) {
                        cnt++;
                    }
                }
            }
            System.out.println(cnt);
        }
        sc.close();
    }
}
