class Solution {
    public int[] solution(long n) {
        String s = n + "";
        String[] str = s.split("");
        int[] answer = new int[str.length];
        for (int i = 0; i < str.length; i++) {
            answer[str.length - i - 1] = Integer.parseInt(str[i]);
        }
        return answer;
    }
}