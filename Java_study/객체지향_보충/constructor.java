package Java_study.객체지향_보충;

public class constructor {
    public static void main(String[] args) {
        // 생성자는 인스턴스가 호출될때마다 iv를 초기화 해주는 메서드
        // 클래스명과 이름이 같고 return이 없다 void도 안붙임
        // 모든 클래스는 생성자를 가짐
        // Ex) Class c=new Class()<-(기본)생성자 호출임 
        // 기본생성자가 있더라도 항상 클래스에는 직접 생성자를 만들어주는 습관을 가지자

        // 원래는
        any_class1 ac1=new any_class1();
        ac1.value=10;

        // 생성자를 잘쓰면
        any_class2 ac2=new any_class2(20);

        System.out.println(ac1.value); //10
        System.out.println(ac2.value); //20

    }
}

class any_class1{
    int value;
    // 컴파일러가 자동으로 생성자 추가
}

class any_class2{
    int value;
    any_class2(){} // <-직접 기본생성자 외의 생성자를 만들경우 기본생성자도 수동으로 추가해줘야함

    any_class2(int x){
        value=x;
    }
}

class any_class3{
    String color;
    String gearType;
    int door;
    // 생성자 this()는 생성자에서 다른 생성자를 호출할 때 사용
    // 다른 생성자 호출시 첫 줄에서만 사용 가능

    // 밑의3개 생성자는 모두 iv초기화, 오버로딩과 비슷한 개념
    // 코드의 중복을 제거하기 위해 서로 호출하는 경우가 많음

    // 디폴드값
    any_class3(){
        // 세번째 생성자 호출로 코드 중복 줄임
        this("White","auto",4);
    }
    any_class3(String color){
        this(color,"auto",4);
    }
    // 참조변수 this는 생성자 this와 전혀 별개. 인스턴스 자신을 가리키는 참조변수.
    // 인스턴스 메소드(생성자 포함)에서 사용가능
    // 지역변수와 인스턴스 변수를 구별할 때 사용
    any_class3(String color, String gearType, int door){
        this.color=color;
        this.gearType=gearType;
        this.door=door;
    }
}
