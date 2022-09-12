import java.util.*;

class 문자열_내림차순으로_배치하기 {
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