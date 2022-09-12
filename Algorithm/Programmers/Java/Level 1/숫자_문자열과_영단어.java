class 숫자_문자열과_영단어 {
    public int solution(String s) {
        String[] dictionary = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
        for (int i = 0; i < 10; i++) {
            s = s.replace(dictionary[i], i + "");
        }
        return Integer.parseInt(s);
    }
}