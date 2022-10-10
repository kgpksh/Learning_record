package Java_study.객체지향_보충;

public class reason_for_polymorphism {
    public static void main(String[] args) {
//        다형성은 조상타입의 배열에 자손들의 객체를 담을 수 있다는 장점도 있다.

    }


}
class Buyer{
    int money=1000;
    int bonusPoint=0;


//    다형성을 이용하지 않았을때 모든 상품들에 대해 일일히 메서드 만들어줘야함
    void buy_audio(Audio a){
        money-=a.price;
        bonusPoint+=a.bonusPoint;
    }
    void buy_computer(Computer c){
        money-=c.price;
        bonusPoint+=c.bonusPoint;
    }

//    다형성을 이용했을때 모든 상품들의 조상인 Product를 이용하여 한번만 함수작성

    void buy(Product p){
        money-=p.price;
        bonusPoint+=p.bonusPoint;
    }
}
class Product{
    int price;
    int bonusPoint;
}

class Audio extends Product{}
class Computer extends Product{}