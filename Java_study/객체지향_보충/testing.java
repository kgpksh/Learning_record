package Java_study.객체지향_보충;

import java.util.*;

public class testing {
    public static void main(String[] args) {
        Calling2 calling2 = new Calling2();
        calling2.ppring("asdf");
    }
    private static void adder(Map<String,Integer> map) {
        map.put("a",map.get("a")+1);
    }


    public static Comparator<Map.Entry<String,Integer>> myComperator = new Comparator<Map.Entry<String,Integer>>() {
        @Override
        public int compare(Map.Entry<String,Integer> o1, Map.Entry<String,Integer> o2) {
            int leftScore = o1.getValue();
            int rightScore = o2.getValue();
            if (leftScore == rightScore) {
                String leftName = o1.getKey();
                String rightName = o2.getKey();
                return leftName.compareTo(rightName);
            }
            return (rightScore - leftScore);
        }
    };

    static class My {
        String name;
        int score;
        My(String name, int score) {
            this.name = name;
            this.score = score;
        }
    }

}
