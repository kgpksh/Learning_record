package Java_study.자바_보충;

public class LambDa {

    int max(int a, int b) {
        return a > b ? a : b;
    }
//            메서드의 이름과 반환 타입을 제거하고  ->를 { 앞에 붙임
//    (int a, int b) -> {
//        return a > b ? a : b;
//    }

//    반환 값이 있는 경우 식이나 값만 적고 return, ; 안붙임
//    (int a, int b) -> a > b ? a : b

//    매개 변수의 값이 추론 가능하면 생략 가능(대부분의 경우 생략 가능)
//    (a, b) -> a > b ? a : b

//    매개변수가 하나 일 때는 괄호 생략 가능
//    타입이 있을 경우 생략 불가
//    a -> a * a
//    (int a) -> a * a

//    실제로 쓰려면 아래와 같이 람다식이라는 익명 '객체'라는 것을 이용 한다.
//    new Object() {
//        int max(int a, int b) {
//            return a > b ? a : b;
//        }
//    };

    public static void main(String[] args) {
//        기본형
        AddFunction f1 = new AddFunction() {
            @Override
            public int max(int a, int b) {
                return a > b ? a : b;
            }
        };
//        다음과 같이 람다식으로 구현 할 수 있음
        AddFunction f2 = (a,b) -> a > b ? a: b;

        int value = f2.max(3,4);
    }

}

//함수형 인터페이스: 하나의 추상 메서드만 가지고 있는 인터페이스

@FunctionalInterface
interface AddFunction {
    public abstract int max(int a, int b);
}
