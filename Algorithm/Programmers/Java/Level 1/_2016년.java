public class _2016년 {
    public String solution(int a, int b) {
        String[] days={"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
        int day=0;
        
        if(a==1){
            return days[(b-1)%7];
        }
        
        for(int i=1; i<a; i++){
            if(i==2){
                day+=29;
            }else if(i<8){
                if(i%2==0){
                    day+=30;
                }else{
                    day+=31;
                }
            }else{
                if(i%2==0){
                    day+=31;
                }else{
                    day+=30;
                }
            }
        }
        
        day+=b-1;
        return days[day%7];
    }
}
