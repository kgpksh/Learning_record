import java.util.*;

class 정수_내림차순으로_배치하기 {
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