class 콜라츠_추측 {
    public int solution(int num) {
        int cnt = 0;
        if (num == 1) {
            return 0;
        }
        while (true) {
            if (num == 1) {
                return cnt;
            }
            if (cnt == 500) {
                return -1;
            }

            if (num % 2 == 0) {
                num /= 2;
            } else if (num % 2 == 1) {
                num = num * 3 + 1;
            }
            cnt++;
        }
    }
}