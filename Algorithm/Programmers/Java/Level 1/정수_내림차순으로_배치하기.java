import java.util.*;

class Solution {
    public long solution(long n) {
        String s = n + "";
        String[] str = s.split("");
        Arrays.sort(str, Collections.reverseOrder());
        StringBuffer sb = new StringBuffer();
        for (String num : str) {
            sb.append(num);
        }
        return Long.parseLong(sb.toString());
    }
}