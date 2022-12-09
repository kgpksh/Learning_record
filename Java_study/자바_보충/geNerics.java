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

class Product{}
class Tv extends Product{}


class Fruit{}

//Fruit의 자손만 받을 수 있음
class FruitBox<T extends Fruit>{}