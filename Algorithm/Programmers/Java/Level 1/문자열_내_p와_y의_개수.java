class Solution {
    boolean solution(String s) {
        s = s.toUpperCase();
        int p = counter(s, "P");
        int y = counter(s, "Y");
        if (p == y) {
            return true;
        }
        return false;
    }

    int counter(String s, String c) {
        return s.length() - s.replace(c, "").length();
    }
}