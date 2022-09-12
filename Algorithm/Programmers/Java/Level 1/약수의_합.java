class 약수의_합 {
    public int solution(int n) {
        if (n == 0) {
            return 0;
        }
        int answer = 0;
        int s = (int) Math.sqrt(n);

        for (int i = 1; i < s + 1; i++) {
            if (n % i == 0) {
                answer += i;
                answer += n / i;
            }
        }
        if (s * s == n) {
            answer -= s;
        }
        return answer;
    }
}