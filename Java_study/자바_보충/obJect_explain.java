package Java_study.자바_보충;

public class obJect_explain {
    public static void main(String[] args) {
        Obj obj=new Obj();

//        객체 자신의 복사본 반환
//        protected obj.clone();

//        객체자신과 object가 같은 객체인지 알려준다
//        obj.equals(Object object);

//        객체 자신의 정보를 문자열로 반환
        obj.toString();


//        객체가 소멸될 때 가비지 컬렉터에 의해 자동 호출. 이때 수행되어야 하는 코드가 있을 때 오버라이딩. 거의 사용안함 급하게 메모리 확보해야 하는데 시간이 걸리기때뭉
//        protected obj.finalize();


//        protected가 붙은건 오버라이딩 시 public으로 변경해야 쓸수 있음

//        객체 자신의 클래스 정보를 담고 있는 Class 인스턴스 반환. 이 설계도를 가지고 객체생성, 정보획득을 가능하게 하는 것을 Reflection API라고함
        obj.getClass();
    }
}

class Obj extends Object{}