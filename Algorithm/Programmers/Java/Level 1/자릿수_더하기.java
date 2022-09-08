import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        String s = n + "";
        String[] str = s.split("");
        for (String num : str) {
            answer += Integer.parseInt(num);
        }
        return answer;
    }
}