package Java_study.자바_보충;

import java.util.Arrays;
import java.util.Comparator;

public class compare_comparator {
    public static void main(String[] args) {
//        Comparable : 기본정렬기준, Comparator : 기본정렬기준 외
        String[] str1={"cat","Dog","lion","tiger"};

//        객체베열에 저장된 객체가 구현한 Comparable이 있을경우 2번째 매개변수 X
        Arrays.sort(str1);

//        대소문자 구분 무시, Comperator
        Arrays.sort(str1,String.CASE_INSENSITIVE_ORDER);


//        역순 정렬
        Arrays.sort(str1,new Descending());
    }
}


class Descending implements Comparator{
    public int compare(Object o1, Object o2){
        if (o1 instanceof Comparable && o2 instanceof Comparable){
            Comparable c1=(Comparable) o1;
            Comparable c2=(Comparable) o2;
            return c1.compareTo(c2) * -1;
        }
        return -1;
    }

}