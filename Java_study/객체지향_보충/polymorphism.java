package Java_study.객체지향_보충;

// 참조변수의 형변환은 참조변수(리모콘)을 변경함으로써 사용할 수 있는 멤버의 갯수를 조절하기 위해 함
public class polymorphism {
    TV tv=new TV();
    
//  SmartTV중 원래 TV에 있던거밖에 통제못함
    TV t=new SmartTV();
    
//    불가능 자손타입으로 조상타입 가리킴
//    SmartTV stv=Tv();
    
    
//    조상-자손사이의 관계에서는 형변환 가능

    SmartTV stv=new SmartTV();

//  부모자식간에 참조변수의 형변환 가능
    TV tv2=(TV)stv;
    SmartTV stv2=(SmartTV) tv2;

//  위에서 원래 smartTV, 형변환된 TV, 다시 형변환된 smartTV는 모두 같은 메모리 주소를 가리키고 있다
//    객체에서 사용가능한 참조변수의 갯수를 늘였다 줄였다 하는것이 형변환


    public static void main(String[] args) {

//      컴파일에는 문제없지만 실행시 오류. 처음 TV객체는 caption 메서드가 없는 인스턴스이기 때문에 형변환해도 사용 불가능
        TV television = new TV();
        SmartTV smartTV = new SmartTV();
//        SmartTV smartTV = (SmartTV) television;
//        smartTV.caption();
    }

//  형변환 하기전에 instanceof로 가능여부 확인 필요
//    매개변수에 new TV(), new SmartTV()등 가능
//    예를들어 형제관계면 불가능 판정
    void doWork(TV television){
//        자기 자신과 조상들도 다 참이나옴
        System.out.println(television instanceof Object); //true
        if (television instanceof SmartTV){
            SmartTV smartTV=(SmartTV) television;

        }
    }
}

class TV{
    boolean power;
    int channel;

    void power(){ power=!power;}
    void channelUp(){++channel;}
    void channelDown(){--channel;}
}

class SmartTV extends TV{
    String text;
    void caption(){System.out.println("CAPTION");}
}
