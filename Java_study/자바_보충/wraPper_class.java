package Java_study.자바_보충;

public class wraPper_class {

//    기본형을 감싸는 클래스.
//    8개의 기본형을 객체로 다뤄야 할 때 쓰는 클래스
//    자바는 비 객체지향적인 기본 자료형이 있다. 이를 보조해주는 것.



    public static void main(String[] args) {
        //    Number 클래스는 모든 숫자클래스의 조상. 래퍼클래스를 기본형을 바꿔주는 메서드가 있음
        Integer integer=new Integer(4234);
        int changed_integer=integer.intValue();


//        오토박싱, 언박싱
//        JDK1.5 이전까지는 기본형과 참조형간의 연산 불가능
        Integer iObj=new Integer(4);
        int i=5;
        int sum=i+iObj;
//        컴파일러가 다음과 같이 자동으로 바꾼다
//        int sum=i+iObj.intValue();
    }
}
