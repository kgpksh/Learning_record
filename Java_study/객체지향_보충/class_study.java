package Java_study.객체지향_보충;
// 소스파일 하나당 0~1개의 public class 존재가능

public class class_study {
    public static void main(String[] args) {
        // 객체배열==참조변수 배열
    another_class class1,class2,class3;
    // -> 같음
    another_class[] classes=new another_class[3];
    // 배열만 만든다고 되는게 아님
    // 배열안에 각각 새롭게 객체를 만들어줘야함
    classes[0]=new another_class();
    classes[1]=new another_class();
    classes[2]=new another_class();
    // cv는 객체와 관계없이 공유됨, 공통속성
    classes[0].cv=4;
    classes[1].cv=7;
    
    classes[0].iv=5;
    classes[1].iv=9;
    System.out.println(classes[0].cv);
    System.out.println(classes[1].cv);

    // cv는 클래스명.속성으로 바로 부르기 가능
    System.out.println(another_class.cv);
    }
}

// 여러개의 일반 클래스는 가능
// 그러나 소스파일당 하나의 클래스만 존재하는것이 바람직
// 또한 소스파일명과 같은 클래스가 있을 경우 실행시 엉뚱한 결과가 나올 수 있음
class another_class{
    // 클래스 영역에는 선언만 가능


    // 인스턴스 변수, 객체생성시 생성
    int iv;
    // 클래스 변수(static 변수, 공유변수), 클래스가 메모리에 올라갈때 생성
    static int cv;
    void method(){
        // 지역변수
        int lv=0;
    }
}