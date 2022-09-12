class 정수_제곱근_판별 {
    public long solution(long n) {
        double s = Math.sqrt(n);
        if (s % 1 == 0) {
            return (long) Math.pow(s + 1, 2);
        } else {
            return -1;
        }
    }
}