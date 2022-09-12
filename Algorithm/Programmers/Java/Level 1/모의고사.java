import java.util.*;
public class 모의고사 {
    public int[] solution(int[] answers) {
        int[] a={1,2,3,4,5};
        int[] b={2, 1, 2, 3, 2, 4, 2, 5};
        int[] c={3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] rec={0,0,0};
        for(int i=0; i<answers.length; i++){
            int correct=answers[i];
            
            if (a[i%5]==correct){
                rec[0]+=1;
            }
            if (b[i%8]==correct){
                rec[1]+=1;
            }
            if (c[i%10]==correct){
                rec[2]+=1;
            }            
        }
        
        int m=0;
        for (int r:rec){
            m=Math.max(m,r);
        }
        
        ArrayList<Integer> tmp = new ArrayList();
        for (int i=0; i<rec.length; i++){
            if (rec[i]==m){
                tmp.add(i+1);
            }
        }
        int[] answer=new int[tmp.size()];
        int index=0;
        for(Integer i:tmp){
            answer[index++]=i;
        }
        return answer;
    }
}
