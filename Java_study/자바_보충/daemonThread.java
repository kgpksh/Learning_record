package Java_study.자바_보충;

public class daemonThread {
//    데몬 쓰레드는 보조 쓰레드. 일반 쓰레드가 모두 종료되면 자동적으로 종료. EX) 가비지 컬렉터, 자동저장, 화면 자동갱신

    public static void main(String[] args) {
//        데몬쓰레드는 start() 하기 전에 setDaemon()으로 지정해줘야 한다. 안그러면 IllegalThreadStateException 발생
        Thread th = new Thread(new daeMon());
        th.setDaemon(true);
    }
}

//무한루프와 조건문을 이용해서 실행 후 대기하다 특정조건이 만족되면 작업을 수행하고 다시 대기
class daeMon implements Runnable {
    boolean autoSave = true;
    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(3000);
            } catch (InterruptedException interruptedException) {

            }

            if (autoSave) {
                saveAuto();
            }
        }
    }

    static void saveAuto() {
        System.out.println("SAVED");
    }
}
