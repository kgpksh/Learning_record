package Algorithm.Baekjoon.Java.문자열;

import java.util.*;

public class 다이얼 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, Integer> map = new HashMap<String, Integer>() {
            {
                put("A", 3);
                put("B", 3);
                put("C", 3);
                put("D", 4);
                put("E", 4);
                put("F", 4);
                put("G", 5);
                put("H", 5);
                put("I", 5);
                put("J", 6);
                put("K", 6);
                put("L", 6);
                put("M", 7);
                put("N", 7);
                put("O", 7);
                put("P", 8);
                put("Q", 8);
                put("R", 8);
                put("S", 8);
                put("T", 9);
                put("U", 9);
                put("V", 9);
                put("W", 10);
                put("X", 10);
                put("Y", 10);
                put("Z", 10);

            }
        };
        int answer = 0;
        String[] phone = sc.nextLine().split("");
        sc.close();
        for (String s : phone) {
            answer += map.get(s);
        }
        System.out.println(answer);
    }
}
