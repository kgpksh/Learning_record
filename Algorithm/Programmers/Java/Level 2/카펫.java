public class 카펫 {
    public int[] solution(int brown, int yellow) {
        int size = brown + yellow;
        for(int i = 3; i < size; i++) {
            if(size % i != 0) {
                continue;
            }
            
            if((i - 2) * ((size / i) - 2) == yellow) {
                int[] answer = new int[2];
                answer[0] = Math.max(i, size / i);
                answer[1] = Math.min(i, size / i);
                return answer;
            }
        }
        return null;
    }
}
