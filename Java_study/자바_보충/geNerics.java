package Java_study.자바_보충;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class geNerics {
    public static void main(String[] args) {
        //    지네릭스란 컴파일시 타입을 체크해주는 기능
        ArrayList<Integer> arrayList=new ArrayList<>();
        arrayList.add(4);

//        다음과 같이 잘못된 타입이 들어가면 컴파일러가 잡아줌
//        arrayList.add("5");
        arrayList.add(6);

//        꺼낼때 (Integer)같이 형변환 할 필요가 없음
        Integer i=arrayList.get(0);

//        원래대로 여러 종류의 객체를 넣고 싶으면 안에 Object를 넣으면 됨

//        다음과 같이 참조변수와 생성자의 대입된 타입은 일치해야함
        List<Product> tvlist=new ArrayList<Product>();

//        오류
//        List<Product> tvList2=new ArrayList<Tv>();

//        지네릭 클래스간의 다형성은 성립(여전히 대입된 타입은 일치해야)
        List<Tv> tvList2=new ArrayList<Tv>();
        List<Tv> tvList3=new LinkedList<Tv>();

//        매개변수의 다형성 성립
        tvlist.add(new Product());
        tvlist.add(new Tv());

//        원 타입이 Product이기 때문에 첫번째는 형변환 불필요. 두번째는 Tv로 형변환 필요.
        Product product=tvlist.get(0);
        Tv tv=(Tv)tvlist.get(1);

    }
}

class Box<T> {

//    와일드 카드의 상한 제한, T와 그 자손들만 가능
//    List<? extends T> list = new ArrayList();

//    와일드 카드의 하한제한, T와 그 조상들만 가능
//    List<? super T> list2 = new ArrayList();

//    제한 없음, ? extends Object 와 동일
//    List<?> list3 = new ArrayList();

//    메서드의 매개변수에도 사용 가능 Fruit가 들어있는 FruitBox만 넣을 수 있음
    void method(FruitBox<? extends Fruit> box) {}

//    지네릭 메서드. 클래스의 타입 변수 T 와 메서드의 타입 변수 T는 별개
    <T> void sort(List<T> list) {}
//    static 멤버에 타입 변수 사용 불가
//    static T item;

//    타입 변수로 배열 선언은 가능
    T[] itemArr;
//    배열(뿐만 아니라 객체) 생성할 때 타입 변수 사용 불가 쉽게 말해 new 다음에는 T 오는것이 불가능
//    T[] itemArr2 = new T[4];
    ArrayList<T> list = new ArrayList<T>();
    void add(T item) {
        list.add(item);
    }

    T get(int i) {
        return list.get(i);
    }

    int size() {
        return list.size();
    }

    public String toString() {
        return list.toString();
    }
}

interface Eatable{}


// Fruit 클래스와 Eatable 인터페이스를 상속한 것만 받는다는 의미
class FruitBox<T extends Fruit & Eatable> extends Box<T> {}

class Product{}
class Tv extends Product{}


class Fruit{}