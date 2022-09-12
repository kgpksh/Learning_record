class 최소직사각형 {
    public int solution(int[][] sizes) {
        int[] comparer = { 0, 0 };
        for (int[] arr : sizes) {
            int a = Math.min(arr[0], arr[1]);
            int b = Math.max(arr[0], arr[1]);
            comparer[0] = Math.max(a, comparer[0]);
            comparer[1] = Math.max(b, comparer[1]);
        }
        return comparer[0] * comparer[1];
    }
}