class 문자열_다루기_기본 {
    public boolean solution(String s) {
        if (s.length() != 4 && s.length() != 6) {
            return false;
        }
        for (char c : s.toCharArray()) {
            if (!((int) c >= (int) '0' && (int) c <= (int) '9')) {
                return false;
            }
        }
        return true;
    }
}