package Java_study.자바_보충;

import java.lang.annotation.*;
import java.lang.reflect.Field;
import java.lang.reflect.Type;

public class AnnoTation extends parent{

//    오버라이드 되지 않은 메서드 였으면 오류남
    @Override
    void overRide() {
        System.out.println("asdf");
    }

//    더이상 사용 권장 안하는 메서드
    @Deprecated
    static void annoTation() {
//        컴파일 시에 경고
//        경고 내용을 더 자세히 보고 싶다면 cmd에서 javac - Xlint: deprecation {소스파일명}.java 입력
    }

//    경고메세지가 나타나지 않게 억제
//    @SuppressWarnings("unchecked") 예를 들어 unchecked 관련 예외가 나오는 것을 억제
//    @SuppressWarnings("deprecation") 예를 들어 depression 관련 예외가 나오는 것을 억제


//    메타애너테이션은 애너테이션을 만드는 애너테이션이다.
//    @Target({TYPE, FIELD, METHOD ... 등등})
//    @Retention() 에너테이션이 유지 되는 기간
//    SOURCE : 소스 파일에만 존재. CLASS : 클래스 파일에만 존재, 실행시에 사용 불가, 기본값. RUNTIME: 클래스 파일에 존재, 실행시 사용가능

//    @Override는 소스 파일에만 존재하므로 다음과 같이 만들어진다
//    @Target(ElementType.METHOD)
//    @Retention(RetentionPolicy.SOURCE)
//    public @interface Override {}


//    @Inherited
//    애너테이션을 자손 클래스에 상속하고자 할때
    public static void main(String[] args) {
        annoTation();
        }
    }

class parent {
    void overRide() {}
}


//    함수형 인터페이스에 붙이면 컴파일러가 올바르게 작성 했는지 체크. 안붙여도 상관 없지만
@FunctionalInterface
interface func {
//    하나의 메서드만 있어야 함
    void test();
//    void check();
}
