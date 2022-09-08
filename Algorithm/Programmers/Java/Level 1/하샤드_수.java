class Solution {
    public boolean solution(int x) {
        String[] s = Integer.toString(x).split("");
        int sum = 0;
        for (String str : s) {
            sum += Integer.parseInt(str);
        }
        if (x % sum == 0) {
            return true;
        }
        return false;
    }
}