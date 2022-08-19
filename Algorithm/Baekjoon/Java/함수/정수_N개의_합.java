package Algorithm.Baekjoon.Java.함수;

public class 정수_N개의_합 {
    long sum(int[] a) {
        long ans = 0;
        for (int i : a) {
            ans += i;
        }
        return ans;
    }
}
