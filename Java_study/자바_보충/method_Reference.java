package Java_study.자바_보충;

import java.util.function.Function;

public class method_Reference {
//    static, 인스턴스 메서드 참조 : ClassName::method 형식. 람다식을 더 간단히 한 것이다.
    public static void main(String[] args) {
        Function<String, Integer> f = (String s) -> Integer.parseInt(s);
//        위의 것을 다음과 같이 변환
        Function<String, Integer> reference = Integer::parseInt;
    }
}
