class Solution {
    public int solution(int n) {
        if(n == 1) {
            return 1;
        }
        
        if(n == 2) {
            return 2;
        }
        
        int a = 1;
        int b = 2;
        for(int i = 3; i <= n; i++) {
            int tmp = (a + b) % 1000000007;
            a = b;
            b = tmp;
        }
        return b;
    }
}