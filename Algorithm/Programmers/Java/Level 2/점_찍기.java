class Solution {
    public long solution(int k, int d) {
        long answer = 0;
        long R = (long) d * d;
        for(long x = 0L; x <= d; x += k){
            long y = (long) Math.sqrt(R - (x * x));
            answer += (y / k) + 1;
        }
        return answer;
    }
}