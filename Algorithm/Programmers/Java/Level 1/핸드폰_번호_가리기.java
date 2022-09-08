class Solution {
    public String solution(String p) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < p.length() - 4; i++) {
            sb.append("*");
        }
        return sb.toString() + p.substring(p.length() - 4);
    }
}