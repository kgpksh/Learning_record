package Java_study.객체지향_보충;

public class abstract_class {
    public static void main(String[] args) {
        //    추상클래스는 인스턴스를 만드는게 불가능
//        Player p=new Player(); <-오류


//        다음과 같이 구현
        AudioPlayer ap=new AudioPlayer();
        Player aup=new AudioPlayer();


    }
}


//{}(몸통)이 없는 미완성 추상메서드를 가진 미완성 추상클래스
//다른 클래스를 작성하는데 도움을 주기위함
//추상메서드를 쓰면 다른사람이 구현하도록 강제할 수 있다
abstract class Player{
    boolean Pause;
    int currentPos;

//    추상메서드 꼭 필요하지만 자손마다 다르게 구현될 것으로 예상되는 경우
    abstract void play(int pos);
    abstract void stop();


//    다음과 같은 방식도 가능 어차피 바깥은 인스턴스 메서드는 객체생성후 호출가능
    void play(){
//        안쪽에껀 추상메서드
        play(currentPos);
    }
}

class AudioPlayer extends Player{
    void play(int pos){
        System.out.println("Play Audio "+pos);
    }
    void stop(){
        System.out.println("Stop");
    }

}

//다음과 같이 미완성 구현 된 추상 클래스 자손도 가능
abstract class AbstractPlayer extends Player{
    void play(int pos){
        System.out.println("Abstract Play");
    }
}
