package Algorithm.Baekjoon.Java.기본_수학_1;

import java.util.*;

public class ACM_호텔 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int tc = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < tc; i++) {
            String[] str = sc.nextLine().split(" ");
            int h = Integer.parseInt(str[0]);
            int n = Integer.parseInt(str[2]);

            int room = (n / h);
            int floor = n % h;

            if (floor == 0) {
                floor = h;
            } else {
                room++;
            }
            String r = Integer.toString(room);
            if (r.length() == 1) {
                r = "0" + r;
            }
            System.out.println(Integer.toString(floor) + r);
        }
        sc.close();
    }
}
