package Java_study.자바_보충;

public class thRead {
    public static void main(String[] args) {
//        상속된 스레드 실행
        threadExample1 th = new threadExample1();
        th.setPriority(7); // 스레드의 우선순위 지정 자바는 기본 5로 1 ~ 10까지, 윈도우는 32단계 하지만 어쨋건 희망사항일 뿐


//        인터페이스 구현된 스레드 실행
        Runnable r = new threadExample2();
        Thread t = new Thread(r);
        t.setPriority(5); // 스레드의 우선순위 지정 자바는 기본 5로 1 ~ 10까지, 윈도우는 32단계 하지만 어쨋건 희망사항일 뿐
//        위의 2줄을 1줄로 줄일 수 있음
//        Thread t = new Thread(new threadExample2());

        th.start();
        t.start();

//        쓰레드 그룹. 서로 관련된 쓰레드들을 묶어서 다루기 위한 것. 모든 쓰레드는 반드시 하나의 쓰레드 그룹에 포함되어 있어야 함.
//        쓰레드 그룹을 지정하지 않고 생성된 쓰레드는 main 쓰레드 그룹에 속한다.
//        자신을 생성한 쓰레드(부모 쓰레드)의 그룹과 우선순위를 상속받는다
    }
}

// 방법 1. 스레드를 상속. 자바는 단일 상속밖에 안되기 때문에 다른것을 상속 못받음
class threadExample1 extends Thread {
    public void run() {
        /* 작업 내용 */
        for (int i = 0; i < 500; i++) {
//            System.out.println(i + " -1번");
            System.out.println(this.getName()); // 조상인 Thread의 getName() 호출
        }
    }
}
// 방법 2. 인터페이스로 구현
class threadExample2 implements Runnable {
    @Override
    public void run() {
        /* 작업 내용 */
        for (int i = 0; i < 500; i++) {
//            System.out.println(i + " -2번");
            System.out.println(Thread.currentThread().getName()); // 현재 실행중인 Thread를 반환
        }
    }
}