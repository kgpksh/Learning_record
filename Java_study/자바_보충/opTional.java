package Java_study.자바_보충;

import java.util.Optional;
import java.util.OptionalInt;

public class opTional {
//    optional은 어떤 타입 T의 wrapper클래스이다. 특히 null에대해 안전한 취급을 하기 위해 유용하다.

    public static void main(String[] args) {
        String str = "abc";

        Optional<String> op1 = Optional.of(str);
        Optional<String> op2 = Optional.of(null); //NPE 발생
        Optional<String> op3 = Optional.ofNullable(null); //괜찮음

//        빈 옵셔널 객체를 만들때는
        Optional<String> empty1 = null; //바람직 하지 않음
        Optional<String> empty2 = Optional.<String>empty(); //OK. <String>은 생략 가능

//        Optional에서 값 가져오기
        String string1 = op2.get(); //null이면 예외 발생
        String string2 = op2.orElse(""); //null이면 "" 반환
        String string3 = op2.orElseGet(String::new); //람다식 사용 가능 매개변수로 Supplier 공급
        String string4 = op2.orElseThrow(NullPointerException::new); // 널이면 예외 발생 위에비해 예외 종류 지정 가능

//        isPresent 는 널이 아니면 작업 수행 널이면 아무것도 안하
        if (Optional.ofNullable(str).isPresent()) {
            System.out.println(str);
        }

//        기본형만을 위한 옵셔널들도 있다.
        OptionalInt optionalInt = OptionalInt.of(3);
        int three = optionalInt.getAsInt();

//        원래 기본 값은 0으로 초기화됨. 빈 옵셔널인지 0을 넣어준 옵셔널인지 구분해야함
        OptionalInt oi1 = OptionalInt.of(0);
        OptionalInt oi2 = OptionalInt.empty();
        oi1.isPresent();//true
        oi2.isPresent(); //faLse
        oi1.equals(oi2); //false
    }
}
