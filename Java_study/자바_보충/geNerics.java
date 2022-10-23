package Java_study.자바_보충;

import java.util.ArrayList;

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
    }
}
