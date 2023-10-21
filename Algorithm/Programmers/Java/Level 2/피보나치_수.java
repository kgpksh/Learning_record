public class 피보나치_수 {
    public int solution(int n) {
        int one = 0;
        int two = 1;
        for(int i = 2; i <= n; i++) {
            int tmp = (one + two) % 1234567;
            one = two;
            two = tmp;
        }
        return two;
    }
}
