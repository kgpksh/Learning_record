package Algorithm.Baekjoon.Java.브루트포스;

import java.util.*;

public class 체스판_다시_칠하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] init = sc.nextLine().split(" ");
        int n = Integer.parseInt(init[0]);
        int m = Integer.parseInt(init[1]);
        String[] board = new String[n];
        String[] sample = { "WBWBWBWB", "BWBWBWBW" };
        for (int i = 0; i < n; i++) {
            board[i] = sc.nextLine();
        }
        sc.close();

        int answer = 64;
        for (int i = 0; i < n - 7; i++) {
            String[] tmp = Arrays.copyOfRange(board, i, i + 8);
            for (int j = 0; j < m - 7; j++) {
                for (int c = 0; c < 2; c++) {
                    int cnt = 0;
                    for (int t = 0; t < 8; t++) {
                        String tmp2 = tmp[t].substring(j, j + 8);
                        String correct = sample[(t + c) % 2];

                        for (int check = 0; check < 8; check++) {
                            if (tmp2.charAt(check) != correct.charAt(check)) {
                                cnt++;
                            }
                        }

                    }
                    answer = Math.min(answer, cnt);
                }
            }
        }

        System.out.println(answer);
    }
}
