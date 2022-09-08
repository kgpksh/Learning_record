import java.util.*;

class Solution {
    public String solution(String s) {
        String[] str = s.split("");
        Arrays.sort(str);

        StringBuffer sb = new StringBuffer();
        for (String a : str) {
            sb.append(a);
        }

        return sb.reverse().toString();
    }
}