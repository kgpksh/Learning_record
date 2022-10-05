package Java_study.객체지향_보충;

class Data{
    int x;

    // 객체생성없이 클래스명.메서드명으로 바로사용가능
    static long add(long a, long b){
        return a+b;
    }
    // 객체생성후 사용가능
    long add2(long a, long b){
        return a+b;
    }
}

public class kind_of_variable {
    public static void main(String[] args) {
        // 기본형 매개변수와 참조형 매개변수
        // 기본형: 변수의 값을 읽기만 할 수 있다
        // 참조형: 읽고, 변경 할 수 있다
        Data d= new Data();
        d.x=10;
        System.out.println("1 : "+d.x);
        change1(d.x);
        System.out.println("3 : "+d.x);
        change2(d);

        // static은 iv가 없이 파라미터로만 가능, 일반 메서드는 파라미터 없이 iv로 자주 씀
        // static 메서드는 인스턴스 메서드 호출불가


    }
    // 기본형
    static void change1(int x){
        x=1000;
        System.out.println("2 : "+x);
    }

    // 참조형
    static void change2(Data d){
        d.x=1000;
        System.out.println("4 : "+d.x);
    }
}