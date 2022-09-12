import java.util.*;
public class 폰켓몬 {
    public int solution(int[] nums) {
        HashSet<Integer> set=new HashSet();
        for(int i:nums){
            set.add(i);
        }
        int choose=nums.length/2;
        return Math.min(set.size(),choose);
    }
}
