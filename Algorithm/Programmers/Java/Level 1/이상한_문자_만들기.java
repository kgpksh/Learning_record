class Solution {
    public String solution(String s) {
        char[] ch = s.toCharArray();
        int idx = 0;
        for (int i = 0; i < ch.length; i++) {
            if (ch[i] == ' ') {
                idx = 0;
            } else {
                if (idx % 2 == 0) {
                    ch[i] = Character.toUpperCase(ch[i]);
                } else {
                    ch[i] = Character.toLowerCase(ch[i]);
                }
                idx++;
            }
        }
        return new String(ch);
    }
}