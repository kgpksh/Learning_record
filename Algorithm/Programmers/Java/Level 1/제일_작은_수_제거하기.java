import java.util.*;

class 제일_작은_수_제거하기 {
    public int[] solution(int[] arr) {
        Integer m = Arrays.stream(arr).min().getAsInt();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i : arr) {
            list.add(i);
        }
        list.remove(m);
        if (list.size() == 0) {
            list.add(-1);
        }

        return list.stream().mapToInt(i -> i).toArray();
    }
}