package Algorithm.Baekjoon.Java.브루트포스;

import java.util.*;;

public class 덩치 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());

        String[][] two = new String[n][2];

        for (int i = 0; i < n; i++) {
            two[i] = sc.nextLine().split(" ");
        }

        StringBuffer sb = new StringBuffer();
        for (String s[] : two) {
            int order = 1;
            for (String str[] : two) {
                if (Integer.parseInt(s[0]) < Integer.parseInt(str[0])
                        && Integer.parseInt(s[1]) < Integer.parseInt(str[1])) {
                    order++;
                }
            }
            sb.append(order + " ");
        }

        System.out.println(sb);

        sc.close();
    }
}
