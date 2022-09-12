import java.util.*;
class 두_개_뽑아서_더하기 {
    public int[] solution(int[] numbers) {
        HashSet<Integer> set=new HashSet();
        
        for(int i=0; i<numbers.length-1; i++){
            for(int j=i+1; j<numbers.length; j++){
                set.add(numbers[i]+numbers[j]);
            }
        }
        int[] answer = new int[set.size()];
        Iterator iter= set.iterator();
        for(int idx=0; idx<set.size(); idx++){
            answer[idx]=(int)iter.next();
        }
        
        Arrays.sort(answer);
        return answer;
    }
}