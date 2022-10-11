package Java_study.객체지향_보충;

public class interitaance2 {
}

interface Fightable{
    void move(int x, int y);

//    Fightable 인터페이스를 구현한 객체만 매개변수로 받을 수 있다는 뜻
    void attack(Fightable f);
    Fightable method();
}

abstract class unit{
    abstract void move(int x, int y);
}

class Fighter extends unit implements Fightable{
    int x,y;
    public void move(int a, int b){
        x=a;
        y=b;
    }

    public void attack(Fightable f) {

    }
//  인터페이스를 메서드의 리턴타입으로 반환도 가능 (인터페이스를 구현한 클래스의 인스턴스를 반환)
    public Fightable method(){
        return new Fighter();
    }
}
