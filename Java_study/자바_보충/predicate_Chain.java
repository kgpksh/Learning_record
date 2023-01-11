package Java_study.자바_보충;

import java.util.function.Predicate;

public class predicate_Chain {
    public static void main(String[] args) {
        Predicate<Integer> p = i -> i < 100;
        Predicate<Integer> q = i -> i < 200;
        Predicate<Integer> r = i -> i%2 == 100;

        Predicate<Integer> notP = p.negate(); // i>=200
        Predicate<Integer> all = notP.and(q).or(r); // 100<= i && i<200 || i%2 = 0
        Predicate<Integer> all2 = notP.and(q.or(r)); // 100<= i && (i<200 || i%2 = 0)

//        확인법
        all.test(30);

        String str1 = "abc";
        String str2 = "def";
//        등가 비교를 위해서는
        Predicate<String> stringPredicate = Predicate.isEqual(str1);
        Boolean result = stringPredicate.test(str2);

//        위의 2줄을 1줄로 줄이면
//        Boolean result = Predicate.isEqual(str1).test(str2);
        System.out.println(result);
    }
}
