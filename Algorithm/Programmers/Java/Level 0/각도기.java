public class 각도기 {
    public int solution(int angle) {
        if(angle == 180) {
            return 4;
        }
        
        if(angle > 90) {
            return 3;
        }
        
        if(angle == 90) {
            return 2;
        }
        
        return 1;
    }
}
