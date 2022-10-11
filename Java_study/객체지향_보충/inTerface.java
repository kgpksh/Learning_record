package Java_study.객체지향_보충;
//인터페이스란 추상메서들로만 이뤄진 집합이다
//구현된 것이 없는 설계도(모든 멤버가 public)
//추상클래스는 추상메서드가 포함되기만 하면 되지만 인터페이스는 모든게 추상메서드
//인터페이스는 상수,static 메서드, default 메서드로 되어있다
//public, abstract,final은 생략가능
//추상메서드와 인터페이스의 가장 큰 차이점은 iv를 가질 수 있느냐이다

public class inTerface {
    public static void main(String[] args) {
        test t=new test();
        t.mymethod();
    }
}


interface myInterface{
    public static final int value=3;
    public abstract void mymethod();
    
}
interface myInterface2{
    void mymethod2();
    void mymethod3();
}



//인터페이스는 클래스처럼 Object가 최고조상 아님. 인터페이스의 조상은 인터페이스만
//다중상속 가능(조상이 여럿이어도됨)
interface son extends myInterface, myInterface2{}

//인터페이스의 구현으로 추상메서드 완성
class test implements myInterface{
    public void mymethod() {
        System.out.println(value);
    }
}

//추상메서드를 모두 구현하지 않는다면 추상클래스때와 마찬가지로 추상메서드탄생
abstract class test2 implements myInterface2{
    public void mymethod2(){
        System.out.println("mymehthod2");
    }
}