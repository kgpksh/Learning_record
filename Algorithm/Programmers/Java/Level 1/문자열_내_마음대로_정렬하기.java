// Comparer, Comperator 배울것

import java.util.*;

class 문자열_내_마음대로_정렬하기 {
    public String[] solution(String[] strings, int n) {
        String[] tmp = strings;
        for (int i = 0; i < tmp.length; i++) {
            tmp[i] = tmp[i].charAt(n) + tmp[i];
        }

        Arrays.sort(tmp);
        for (int i = 0; i < tmp.length; i++) {
            tmp[i] = tmp[i].substring(1);
        }
        return strings;
    }
}