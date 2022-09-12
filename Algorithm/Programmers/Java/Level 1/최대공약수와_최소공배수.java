class 최대공약수와_최소공배수 {
    int get_gcd(int x, int y) {
        for (int i = Math.min(x, y); i > 0; i--) {
            if (x % i == 0 && y % i == 0) {
                return i;
            }
        }
        return 1;
    }

    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        int gcd = get_gcd(n, m);
        answer[0] = gcd;
        answer[1] = n * m / gcd;
        return answer;
    }
}