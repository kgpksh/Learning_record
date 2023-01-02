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


//        쓰레드를 깨우는 메서드
//        쓰레드의 interrupted 상태를 true로 변경
        t.interrupt();

//        interrupted 되었는지 상태를 반환 한번 인터럽트 되었으면 그 이후론 계속 true
        t.isInterrupted();

//        현재 쓰레드의 interruped상태를 알려주고 false로 초기화
//        static이기 때문에 Thread.으로 시작해야함
//        지금 코드에서는 main 쓰레드가 interrupted 되었는지 확인
        Thread.interrupted();


//        아래는 교착상태에 빠지기 쉬워서 Deprecated된 것들
//        일시정지
        t.suspend();
//        일시정지 해제하고 실행 대기상태로 전환
        t.resume();
//        쓰레드 즉시종료
        t.stop();
    }
}

class joinAndYield {
    public static void main(String[] args) {
        Thread th1 = new Thread(new threadExample2());
        Thread th2 = new Thread(new threadExample2());

        th1.start();
        th2.start();
        long time = System.currentTimeMillis();

        try {
//            두 쓰레드가 끝날 때 까지 main 쓰레드는 대기. 마지막에 최종 소요시간 출력.
            th1.join();
            th2.join();
        } catch(InterruptedException e) {

        }

        System.out.println(System.currentTimeMillis() - time);


//        yield 사용 예시. while문으로 돌리는 중 if에서 일시 정지가 걸리면 busy-waiting 하느니 양보
//        그러나 yield는 OS에게 알려주는 것이므로 반드시 동작한다는 보장은 없다
        boolean stopped = false;
        boolean suspended = false;
        while (!stopped) {
            if (!suspended) {
                /* 작업 수행 */
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {

                }
            } else {
                Thread.yield();
            }
        }
    }


}


// 방법 1. 스레드를 상속. 자바는 단일 상속밖에 안되기 때문에 다른것을 상속 못받음
class threadExample1 extends Thread {
    public void run() {
        /* 작업 내용 */
        for (int i = 0; i < 500; i++) {
//            System.out.println(i + " -1번");
            System.out.println(this.getName()); // 조상인 Thread의 getName() 호출


//            sleep, yield는 static 메서드로 쓰레드 본인이 직접 해야한다. th.sleep() 같이 외부에서 특정 스레드 지정하는건 불가능
            try {
                Thread.sleep(1000);
                Thread.yield();
            } catch (InterruptedException e) {

            }
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