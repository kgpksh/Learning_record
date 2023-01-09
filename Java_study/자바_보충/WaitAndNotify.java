package Java_study.자바_보충;

import java.util.ArrayList;
import java.util.List;

public class WaitAndNotify {

//    lock은 한 객체에 1개이다. 그런데 외부에서 당장 이뤄 질 수 없는 조건을 요구하면서 lock을 붙잡고 놔두지 않을 경우,
//    wait()으로 잠시 쉬게 할 수 있다.
//    notify()를 쓰면 대기실의 쓰레드중 무작위 1개를 깨운다. notifyAll()을 쓰면 모든 쓰레드를 깨운다.

    public static void main(String[] args) {
        Table table = new Table();
        Thread cook = new Thread(new Cook(table));
        Thread cusOne = new Thread(new Customer(table));
        Thread cusTwo = new Thread(new Customer(table));

        cook.start();
        cusOne.start();
        cusTwo.start();
    }

}

class Table {
    private List<String> dishes = new ArrayList<>();
    private final int MAX_FOOD = 5;

    public int getSize() {
        return MAX_FOOD;
    }

    public void add(String dish) {
        synchronized (this) {
            try {
                if (dishes.size() >= MAX_FOOD) {
//                    만약 요리사가 왔는데 테이블이 꽉 차있으면 손님이 먹을 수 있게 대기시킴
                    wait();

                }

                dishes.add(dish);
//                먹을 손님들을 깨움
                notifyAll();
            } catch (InterruptedException e) {}

        }

    }

    public synchronized void remove(String dishName) {
        while (dishes.size() == 0) {
            try {
//                만약 손님이 먹으러 왔는데 테이블이 비어 있으면 요리사가 음식을 올릴 수 있게 대기시킨다.
                wait();
            } catch (InterruptedException e) {

            }
        }
        if (dishes.contains(dishName)) {
            dishes.remove(dishName);


//            요리사, 혹은 다른 손님들을 깨운다
            notifyAll();
        }
    }

}

class Cook implements Runnable {
    Table table;

    Cook(Table table) {
        this.table = table;
    }
    String[] dishList = {"Hamburger", "Pizza", "Ramen", "Gukbab", "Candy"};
    @Override
    public void run() {
        while (true) {
            int idx = (int)(Math.random() * table.getSize());
            table.add(dishList[idx]);

            System.out.println("New Food!");
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {

            }
        }
    }
}

class Customer implements Runnable {
    Table table;

    Customer(Table table) {
        this.table = table;
    }

    String[] dishList = {"Hamburger", "Pizza", "Ramen", "Gukbab", "Candy"};
    @Override
    public void run() {
        while (true) {
            int idx = (int)(Math.random() * table.getSize());
            table.remove(dishList[idx]);
            System.out.println(Thread.currentThread() + " EAT FOOD");

            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {

            }
        }
    }
}