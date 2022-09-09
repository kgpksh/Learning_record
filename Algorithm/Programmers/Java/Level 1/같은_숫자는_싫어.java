import java.util.*;

class Solution {
    public Object[] solution(int[] arr) {

        int previous = -1;

        List<Integer> list = new ArrayList();

        for (int i : arr) {
            if (previous != i) {
                list.add(i);
            }
            previous = i;
        }
        return list.toArray();
    }
}