class 타겟_넘버 {
    int limit;
    int[] numbers;
    int target;
    int answer = 0;
    
    public int solution(int[] numbers, int target) {
        this.limit = numbers.length;
        this.numbers = numbers;
        this.target = target;
        
        dfs(0, 0);
        return answer;
    }
    
    void dfs(int sum, int depth) {
        if(depth == limit) {
            if(sum == target) {
                answer++;
            }
            return;
        }
        
        dfs(sum + numbers[depth], depth + 1);
        dfs(sum - numbers[depth], depth + 1);
    }
}