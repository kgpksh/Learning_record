class 시저_암호 {
    public String solution(String s, int n) {

        char[] ch = s.toCharArray();

        for (int i = 0; i < s.length(); i++) {
            if (ch[i] >= (int) 'a' && ch[i] <= (int) 'z') {
                int tmp = (int) ch[i] + n;
                if (tmp > (int) 'z') {
                    tmp = tmp + 'a' - 'z' - 1;
                }
                ch[i] = (char) tmp;
            } else if (ch[i] >= (int) 'A' && ch[i] <= (int) 'Z') {
                int tmp = (int) ch[i] + n;
                if (tmp > (int) 'Z') {
                    tmp = tmp + 'A' - 'Z' - 1;
                }
                ch[i] = (char) tmp;
            }
        }

        return new String(ch);
    }
}