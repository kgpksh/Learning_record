class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        try {
            int idx = 0;
            while (true) {
                answer += a[idx] * b[idx];
                idx++;
            }
        } catch (Exception e) {
            return answer;
        }
    }
}