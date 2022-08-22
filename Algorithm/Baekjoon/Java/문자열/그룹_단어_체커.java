package Algorithm.Baekjoon.Java.문자열;

import java.util.*;

public class 그룹_단어_체커 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        int tc = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < tc; i++) {
            HashMap<String, Boolean> map = new HashMap<String, Boolean>();
            String[] str = sc.nextLine().split("");
            String fore = "";
            boolean check = true;
            for (String s : str) {
                if (!fore.equals(s) && map.getOrDefault(s, false)) {
                    check = false;
                    break;
                }
                fore = s;

                if (!map.getOrDefault(s, false)) {
                    map.put(s, true);
                }
            }
            if (check) {
                answer++;
            }

        }
        sc.close();
        System.out.println(answer);
    }
}
