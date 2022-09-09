class Solution {
    public long solution(int price, int money, int count) {

        long sum = (long) price * count * (count + 1) / 2;
        if (money >= sum) {
            return 0;
        }
        return sum - money;

    }
}