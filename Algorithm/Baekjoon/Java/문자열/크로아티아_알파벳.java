package Algorithm.Baekjoon.Java.문자열;

import java.util.*;

public class 크로아티아_알파벳 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        sc.close();

        String[] dic = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
        for (String d : dic) {
            s = s.replace(d, "0");
        }
        System.out.println(s.length());
    }
}
