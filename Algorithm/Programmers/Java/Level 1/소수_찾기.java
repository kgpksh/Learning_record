public class 소수_찾기 {
    public int solution(int n) {
        boolean[] b=new boolean[n+1];
        b[0]=true;
        b[1]=true;
        int answer = 0;
        for(int i=2; i<n+1; i++){
            if(b[i]==false){
                answer++;
                for(int j=i*2; j<n+1; j=j+i){
                    b[j]=true;
                }
            }
        }
        return answer;
    }
}
