class 땅따먹기 {
    int solution(int[][] land) {   
        int length = land.length;
        for(int i = 1; i < length; i++) {
            land[i][0] = max(land[i - 1][1], land[i - 1][2], land[i - 1][3]) + land[i][0];
            land[i][1] = max(land[i - 1][0], land[i - 1][2], land[i - 1][3]) + land[i][1];
            land[i][2] = max(land[i - 1][0], land[i - 1][1], land[i - 1][3]) + land[i][2];
            land[i][3] = max(land[i - 1][0], land[i - 1][1], land[i - 1][2]) + land[i][3];
        }
        
        int answer = 0;
        for(int j = 0; j < 4; j++) {
            answer = Math.max(land[length - 1][j], answer);
        }
        return answer;
    }
    
    int max(int a, int b, int c) {
        int tmp = 0;
        if(a > b) {
            tmp = a;
        } else {
            tmp = b;
        }
        
        if(tmp > c) {
            return tmp;
        }
        
        return c;
    }
}