package Java_study.객체지향_보충;

public class abstract_class2 {
    public static void main(String[] args) {
        Unit[] group=new Unit[3];
        group[0]=new Marine();
        group[1]=new Tank();
        group[2]=new Dropship();
    }
}





//여러 클래스에 공통적으로 적용될 수 있는 부분을 뽑아서 추상클래스로 만듬
abstract class Unit{
//  좌표와 stop는 어느 유닛에나 공통됨
    int x,y;
    void stop(){};

//    공중유닛과 지사유닛은 움직이는게 다르므로 추상메서드로
    abstract void move(int x, int y);
}

class Marine extends Unit{
    void move(int x, int y){}
    void stimPack(){};
}

class Tank extends Unit{
    void move(int x, int y){}
    void changeMode(){}
}

class Dropship extends Unit{
    void move(int x, int y){}
    void load(){}
    void unload(){}
}