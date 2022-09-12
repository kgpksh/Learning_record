import java.util.*;

class 나누어_떨어지는_숫자_배열 {
    public int[] solution(int[] arr, int divisor) {
        int length = 0;

        for (int i : arr) {
            if (i % divisor == 0) {
                length++;
            }
        }

        if (length != 0) {
            int[] answer = new int[length];

            int idx = 0;
            for (int i : arr) {
                if (i % divisor == 0) {
                    answer[idx] = i;
                    idx++;
                }
            }
            Arrays.sort(answer);
            return answer;
        } else {
            int[] answer = { -1 };
            return answer;
        }
    }
}