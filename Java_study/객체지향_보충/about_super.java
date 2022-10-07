package Java_study.객체지향_보충;

public class about_super {
    public static void main(String[] args) {
        Child child=new Child();
        child.method();
    }
}

class Parent{
    int x=10;
}

class Child extends Parent{
    int x=20;
    void method(){
//        자신과 조상멤버를 구분할 때 씀
//        super는 조상 this는 자기자신
//        같은 변수명이 2개 있지 않으면 그냥 둘다 같음
        System.out.println("this x :"+this.x);
        System.out.println("super x :"+super.x);
    }
}

class Point2D{
    int x;
    int y;
    Point2D(int x, int y){
        this.x=x;
        this.y=y;
    }
}

class Point3D2 extends Point2D{
//    super 와 super()는 다르다. super()는 조상의 생성자
//    반드시 생성자 첫줄에 super()호출해야함
    int z;
    Point3D2(int x, int y, int z){
        super(x,y);
//        올바르지 않은 방법
//        this.x=x;
//        this.y=y;
        this.z=z;
    }
}