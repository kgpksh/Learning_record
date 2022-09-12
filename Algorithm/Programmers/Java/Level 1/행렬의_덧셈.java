class 행렬의_덧셈 {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int len = arr1.length;
        int len2 = arr1[0].length;

        int[][] answer = new int[arr1.length][len2];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len2; j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        return answer;
    }
}