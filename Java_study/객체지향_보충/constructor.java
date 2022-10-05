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
