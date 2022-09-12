class 자연수_뒤집어_배열로_만들기 {
    public int[] solution(long n) {
        String s = n + "";
        String[] str = s.split("");
        int[] answer = new int[str.length];
        for (int i = 0; i < str.length; i++) {
            answer[str.length - i - 1] = Integer.parseInt(str[i]);
        }
        return answer;
    }
}