package Java_study.자바_보충;

import java.util.function.*;

public class FunTions {
    public static void main(String[] args) {
//        매개변수도 없고 반환값도 없는 경우 run으로 호출
//        Runnable r = () - > run();

//        출력만 있는 경우 get()으로 호출
        Supplier<Integer> s = () -> (int)(Math.random() * 100) + 1;
        s.get();

//        입력만 있는 경우 accept()로 호출
        Consumer<Integer>  c =  i -> System.out.println(i);
        c.accept(3);

//        입력과 출력이 모두 있는 경우 일반적인 함수 apply()로 호출
        Function<Integer, Integer> f = i -> i % 2;
        f.apply(3);

//        조건식 표현하는데 쓰임(boolean) test()로 호출
        Predicate<String> p = str -> str.length() == 0;
        p.test("asdf");

//        예시와 같이 Bi가 붙으면 매개변수가 2개인 경우도 있다. 함수는 원래 2개였으니 3개가 되며 Supplier는 주기만 해야하니 해당 없음
        BiConsumer<Integer, String> bi= (i,stRing) -> System.out.println(i + stRing);
//        3개 입력 부터는 직접 만들면 됨

//        Function의 자손. 입력과 출력 타입이 일치하는 경우이다.
        UnaryOperator<Integer> u = i ->  i+1;
//        BiFunction의 자손. 입력과 출력 타입이 일치하는 경우이다.
        BinaryOperator<Integer> b = (i,j) -> i+j;


//        두 함수의 연결
        Function<String, Integer> f1 = (str) -> Integer.parseInt(str);
        Function<Integer, String> f2 = i -> Integer.toBinaryString(i);

        Function<String, String> h1 = f1.andThen(f2); // f1 실행 후 결과로 f2실행하는 새로운 함수
        Function<Integer, Integer> h2 = f1.compose(f2); // f2 실행 후 결과로 f2 실행하는 새로운 함수

    }
}
