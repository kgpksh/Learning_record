// Integer.parseInt("String",n) 쓸시 n진법에서 10진법 바로 변환 가능

import java.util.*;

class _3진법_뒤집기 {
    public int solution(int n) {
        int answer = 0;
        List<Integer> number = new ArrayList<Integer>();
        while (true) {
            if (n < 3) {
                number.add(n);
                break;
            } else {
                number.add(n % 3);
                n /= 3;
            }
        }

        int size = number.size();
        for (int i = size - 1; i >= 0; i--) {
            answer += Math.pow(3, i) * number.get(size - i - 1);
        }
        return answer;
    }
}