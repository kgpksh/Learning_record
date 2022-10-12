package Java_study.객체지향_보충;

public class misc {
//    default 메서드 : 인터페이스에 특정 클래스를 위한 메서드가 추가되면 기존에 있던 다른 클래스들이 다 구현해줘야함
//    default 메서드는 인터페이스의 원칙 위반한 예외
//    여러 인터페이스의 default 메서드가 충돌시 오버라이딩 해줘야함
//    디폴트 메서드와 조상클래스가 충돌시 디폴트가 무시됨

    public static void main(String[] args) {
        AA aa=new AA();
//        내부클래스의 객체는 외부클래스의 객체가 있어야 만들 수 있다
        AA.BB aabb=aa.new BB();
    }
}


class aa{
    int i=100;

}

class bb{
    aa a=new aa();
    void method(int i){
        System.out.println(a.i);
    }
}


//    내부클래스에서 외부클래스의 멤버들을 쉽게 접근 할 수 있다.
//    코드의 복잡성을 줄일 수 있다.(캡슐화)
class AA{
    int i=100;
    BB b=new BB();
    class BB{
        void method(){
            System.out.println(i);
        }
    }
}