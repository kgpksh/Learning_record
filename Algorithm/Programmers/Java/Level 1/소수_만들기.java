public class 소수_만들기 {
    public int solution(int[] nums) {
        int answer = 0;
        for(int i=0; i<nums.length-2; i++){
            for(int j=i+1; j<nums.length-1; j++){
                for(int h=j+1; h<nums.length; h++){
                    
                    boolean check=true;
                    int sum=nums[i]+nums[j]+nums[h];
                    for(int p=2; p<(int)(Math.sqrt(sum)+1); p++){
                        if(sum%p==0){
                            check=false;
                            break;
                        }
                    }
                    if(check){
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
}
