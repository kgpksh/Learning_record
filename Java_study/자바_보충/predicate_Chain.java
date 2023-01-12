package Java_study.자바_보충;

import java.util.*;
import java.util.function.BiFunction;
import java.util.function.Consumer;
import java.util.function.Predicate;
import java.util.function.UnaryOperator;

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


//        컬렉션 프레임웍과 함수형 인터페이스 결합응용

        List<Integer> list = new ArrayList<>(Arrays.asList(10, 300, 30, 245, 312));

//        컬렉션 전체 해당 - Predicate에 해당하는 요소 제거
        list.removeIf(p);

//        List에 해당 - 모든 요소들을 해당 기준으로 변환
        UnaryOperator<Integer> uo = i -> i%2;
        list.replaceAll(uo);
        list.replaceAll(i -> i%2);

//        Iterable에 해당 - 모든 요소들에 작업 수행
        Iterable<Integer> it = new ArrayList<>();
//        it.forEach(여기 컨슈머 넣음);

//        Map에 해당
        Map<Integer, Integer> map = new HashMap<>();
        map.put(3,5);
        map.put(2,7);

//        맵의 모든 키 밸류 출력
        map.forEach((k,v) -> System.out.println(k + " " + v));
    }
}
