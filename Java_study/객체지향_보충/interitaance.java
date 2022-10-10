package Java_study.객체지향_보충;

public class interitaance {
    public static void main(String[] args) {
        Circle c=new Circle();
        System.out.println(c.x);
        c.x=15;
        System.out.println(c.x);
    }
}


class Point{
    int x;
    int y;
    Point(){
        x=10;
    }
    String getLocation(){
        return "x :"+ x +", y : "+ y;
    }
}

// 부모클래스 Point를 상속한 자식클래스
class Circle extends Point{
    int r;

    // 오버라이딩
    // 선언부는 일치해야함, 내용만 변경
    // 접근제어자가 조상의 것보다 범위가 같거나 넓어야함
    // 예외는 조상클래스의 메서드보다 많이 선언할 수 없음
    String getLocation(){
        return "x :"+ x +", y : "+ y + "r : "+r;
    }

    // 모든클래스의 조상 Object 클래스의 기본 메서드 toString을 오버라이딩
    public String toString(){
        return "x :"+ x +", y : "+ y + "r : "+r;
    }
}

// 클래스의 포함관계
// 클래스의 멤버로 참조변수를 선언하는것
class Point3D{
    Point p=new Point();
    int z;
}

// 클래스간의 관계 결정하기
// 상속관계 : ~은 ~이다(is - a)
// 포함관계 : ~은 ~을 가지고 있다(has - a)
// 원은 점이다 vs 원은 점을 가지고 있다
// 이경우엔 포함이 적절
// 상속은 꼭 필요할때만