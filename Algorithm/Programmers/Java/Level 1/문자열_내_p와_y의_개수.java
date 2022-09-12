class Solution {
    boolean solut문자열_내_p와_y의_개수ion(String s) {
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