class 핸드폰_번호_가리기 {
    public String solution(String p) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < p.length() - 4; i++) {
            sb.append("*");
        }
        return sb.toString() + p.substring(p.length() - 4);
    }
}