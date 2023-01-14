package Java_study.자바_보충;

import java.util.Arrays;
import java.util.Random;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class stReam {
    public static void main(String[] args) {
//        객체 배열 스트림 만들기
        Integer[] arr = {2,3,4,5};
        Stream<Integer> arrStream1 = Stream.of(2,3,4);
        Stream<Integer> arrStream2 = Stream.of(arr);
        Stream<Integer> arrStream3 = Arrays.stream(arr);
//        배열 일부만
        Stream<Integer> arrStream4 = Arrays.stream(arr, 2,3);

//        비슷하게 기본형 스트림도 만들 수 있음
        IntStream intStream = IntStream.of(2,3,4);

//        일반 스트림에는 count정도밖에 없지만 IntStream에는 sum, average 등도 있다



//        난수를 요소로 갖는 무한스트림
        IntStream is = new Random().ints(); //ints는 int의 최솟값에서 최댓값 범위를 가짐, longs도 있고, doubles의 범위는 0.0 <= d < 1.0까지
        is.limit(5).forEach(System.out::println); //무한 스트림이기 때문에 필요한 만큼 잘라줘야함
        IntStream is2 = new Random().ints(5); //이런 식으로 한줄로 만들 수 도 있음
        IntStream is3 = new Random().ints(5, 10); // 지정된 범위의 난수 만들기 10미만까지임
        IntStream is4 = new Random().ints(3, 5, 10); // 지정된 범위의 난수 3개 구하기

//        특정 범위의 정수 요소 스트림
        IntStream ist = IntStream.range(1,5); // 1,2,3,4
        IntStream ist2 = IntStream.rangeClosed(1,5); // 1,2,3,4,5


        Stream<Integer> iter = Stream.iterate(0, i -> i+2); //iterate는 seed, UnaryOperator를 파라미터로 받는다. 이전 요소에 종속적. 0,2,4... 무한스트림
        Stream<Double> gen = Stream.generate(Math::random);// generator는 seed 없음, Supplier만 파라미터로. 이전 요소에 독립적


//        스트림의 중간연산은 스트림이며 n번 하고, 최종연산은 다른것으로 1번만 한다.

        Stream<Integer> itsr = Stream.of(2,2,3,4,2,1,9); // 생성

        Stream<Integer> middle = itsr.filter(i -> i>1).distinct().sorted(); //중간연산

        middle.forEach(System.out::println); // 최종연산


//        map
        Stream<Integer> integerStream = Stream.of(1,2,3,4,5,6,7);

        integerStream.map(i -> i.toString()); // map을 통해 Integer 스트림에서 String 스트림으로 바뀌었다.


//        flatMap은 스트림의 차원을 줄이는 기능을 한다.
        String[] str1 = {"ab", "cd", "ef"};
        String[] str2 = {"gh", "ij", "kl"};

        Stream<String[]> arrStream = Stream.of(str1,str2);
        Stream<String> flatStream = arrStream.flatMap(Arrays::stream);

        flatStream.forEach(System.out::println); //만약 그냥 map이었으면 문자열 6개 대신 스트림 2개가 출력됨

//        스트림에 .sequential을 적용 하면 직렬, parallel을 적용 하면 멀티 스레드 병렬 스트림.



//        reduce는 스트림의 요소를 하나씩 줄여 가며 누적 연산. identy: 초기값, accumulator: 이전 처리 결과에 수행할 연산, combiner: 병렬 처리 된 결과 합침
//        collect로 그루핑을 할 수 있는데 partitioning으로 2개, groupingby로 그 이상도 나눌 수 있다
    }
}
