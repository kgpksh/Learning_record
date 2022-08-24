package Algorithm.Baekjoon.Java.기본_수학_1;

import java.util.*;

public class 부녀회장이_될테야 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();

        for (int i = 0; i < tc; i++) {
            int k = sc.nextInt();
            int n = sc.nextInt();
            ArrayList<int[]> tmp = new ArrayList<>();

            int[] init = new int[n];
            for (int initialize = 1; initialize < n + 1; initialize++) {
                init[initialize - 1] = initialize;
            }
            tmp.add(init);

            for (int j = 0; j < k; j++) {
                int[] row = new int[n];

                for (int h = 0; h < n; h++) {
                    int adder = add(tmp.get(j), h);
                    row[h] = adder;
                }
                tmp.add(row);
            }

            System.out.println(tmp.get(k)[n - 1]);

        }
        sc.close();
    }

    private static int add(int[] n, int idx) {
        int answer = 0;
        for (int i = 0; i < idx + 1; i++) {
            answer += n[i];
        }
        return answer;
    }

}
