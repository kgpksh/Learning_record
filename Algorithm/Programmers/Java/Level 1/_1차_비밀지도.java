// 자바의 비트연산은 10진수 상태에 바로 적용가능하다

class _1차_비밀지도 {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i = 0; i < n; i++) {
            String element = "";
            String a1 = Integer.toString(arr1[i], 2);
            String a2 = Integer.toString(arr2[i], 2);

            while (a1.length() < n) {
                a1 = "0" + a1;
            }
            while (a2.length() < n) {
                a2 = "0" + a2;
            }

            for (int j = 0; j < n; j++) {
                if (a1.charAt(j) == '0' && a2.charAt(j) == '0') {
                    element += " ";
                } else {
                    element += "#";
                }
            }
            answer[i] = element;
        }
        return answer;
    }
}