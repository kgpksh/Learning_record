package Algorithm.Baekjoon.Java.문자열;

import java.util.*;

public class 단어의_개수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int l = s.length();
        if (l == 0 || l == 1 && s.charAt(0) == ' ') {
            System.out.println(0);
        } else {
            if (s.charAt(0) == ' ') {
                s = s.substring(1);
            }

            if (s.charAt(s.length() - 1) == ' ') {
                s = s.substring(0, l - 1);
            }
            String[] ss = s.split(" ");
            System.out.println(ss.length);
        }
        sc.close();
    }
}
