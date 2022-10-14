package Java_study.자바_보충;

public class hash_string {
    public static void main(String[] args) {
//        hashcode() : Object 클래스의 객체의 주소를 int로 반환해서 주는 메서드. 객체의 지문
//        equals()를 오버라이딩 하면 hashcode()도 오버라이딩 해야함
//        보통 주소에서 iv를 가지고 비교하도록 오버라이딩 하는데 equals의 결과가 true면 두 객체의 해시코드는 같아야 하기 때문
        String str1=new String("abc");
        String str2=new String("abc");
        System.out.println(str1.equals(str2));

//        64비트 jvm으로 바뀌면서 주소값이 겹칠수도 있음. long 타입도 32비트때와 같이 int로 반환하기 때문에

//        해시코드와 동일, 오버라이딩 하기 이전에 기능이 필요할 때 씀
//        객체마다 다른해시코드가 나오게 됨
//        System.identityHashCode(Object obj)
    }
}
