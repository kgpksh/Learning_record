package Java_study.객체지향_보충;

public class initiaizing {
    // 1.자동초기화 : 지역변수는 꼭 사용전 수동초기화, 멤버변수(iv,cv)는 자동초기화됨 ex int x; <=0으로

    // 2.간단초기화 : 멤버변수의 초기화는 =으로 명시적 초기화
    // ex)
    int k=54;
    Tmp tmp=new Tmp();

    // 3.복잡한 초기화 : , 여러문장 넣기에는 초기화 블럭을 사용
    // 인스턴스 초기화 블럭 -> {}
    // 클래스 초기화 블럭 -> static {}

}

class Tmp{
    static int[] arr = new int[10];

    // 클래스 복잡 초기화 예시
    static{
        for(int i=0; i<arr.length; i++){
            arr[i]=(int)(Math.random()*10)+1;
        }
    }
}
