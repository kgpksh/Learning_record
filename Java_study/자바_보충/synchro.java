package Java_study.자바_보충;

public class synchro {

    public static void main(String[] args) {
        Runnable r = new actor();
        new Thread(r).start();
        new Thread(r).start();
    }
    int balance;
//    syncronized를 이용한 동기화.
//    어떤 메서드나 영역 앞에 syncronized를 붙이면 그 영역은 한번에 한 쓰레드 밖에 접근 못한다.

//    예시 1. 메서드 전체 임계영역으로 지정
    synchronized void withdraw(int money) {
        if (balance >= money) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {

            }

            balance -= money;
        }
    }

//    예시 2. 특정한 영역을 임계영역으로 지정
    synchronized void withdraw2(int money) {
        synchronized (this) {
            if (balance >= money) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {

                }

                balance -= money;
            }
        }
    }
}

class Account {
    private int balance = 1000;

//    여기에도 싱크로 붙여줘야함. 읽는 과정에서도 동기화가 되어야 값이 제대로 전달됨.
    public synchronized int getBalance() {
        return balance;
    }

//    싱크로를 안 붙이면 잔고가 음수도 가능하다
    public synchronized void withdraw(int money) {
        if (balance >= money) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {

            }

            balance -= money;
        }
    }
}

class actor implements Runnable{
    Account account = new Account();
    int[] available_spending = {100, 200, 300};
    @Override
    public void run() {
        while (account.getBalance() > 0) {
            int idx = (int)(Math.random() * 3);
            account.withdraw(available_spending[idx]);

            System.out.println(Thread.currentThread()+ " " + available_spending[idx] + " " + account.getBalance());
        }
    }
}