import java.util.*;
class JadenCase_문자열_만들기 {
    public String solution(String s) {
        String[] str = s.split("");
        str[0] = str[0].toUpperCase();
        for(int idx = 1; idx < str.length; idx++) {
            if(str[idx - 1].equals(" ")) {
                str[idx] = str[idx].toUpperCase();
            } else {
                str[idx] = str[idx].toLowerCase();
            }
        }
        return String.join("", str);
    }
}