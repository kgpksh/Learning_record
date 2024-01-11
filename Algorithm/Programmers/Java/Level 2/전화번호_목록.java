import java.util.Arrays;
class 전화번호_목록 {
    public boolean 전화번호_목록(String[] phone_book) {       
        int L = phone_book.length;
        Arrays.sort(phone_book);
        
        for(int idx = 0; idx < L - 1; idx++) {
            if(phone_book[idx + 1].startsWith(phone_book[idx])) {
                return false;
            }
        }
        
        return true;
    }
}