class 두_정수_사이의_합 {
    public long solution(int a, int b) {
        int m = Math.min(a, b);
        int n = Math.max(a, b);
        long answer = 0;
        for (int i = m; i <= n; i++) {
            answer += i;
        }

        return answer;
    }
}