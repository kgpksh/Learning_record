import java.util.*;

class 예산 {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        for (int b : d) {
            if (budget < b) {
                break;
            }
            answer++;
            budget -= b;
        }
        return answer;
    }
}