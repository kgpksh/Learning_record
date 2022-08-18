package Algorithm.Baekjoon.Java.조건문;

import java.util.*;

public class 오븐_시계 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int h, m, t, hour, minute, sigan;

        String inputClac = sc.nextLine();
        String[] arrInputClac = inputClac.split(" ");

        h = Integer.parseInt(arrInputClac[0]);
        m = Integer.parseInt(arrInputClac[1]);

        t = sc.nextInt();

        hour = (t + m) / 60;
        minute = (t + m) % 60;

        sigan = h + hour;
        if (sigan > 23) {
            sigan -= 24;
        }

        System.out.println(sigan + " " + minute);

        sc.close();
    }
}
