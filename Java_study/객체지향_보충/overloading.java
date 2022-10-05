package Java_study.객체지향_보충;

public class overloading {
    // A: 이 둘은 일단 오버로딩이다
    static long add(int a, long b){ return a+b; }
    static long add(long a, int b){ return a+b; }
    public static void main(String[] args) {
        // 오버로딩 : 한 클래스 안에 같은 이름의 메서드 여러개가 있을 수 있음
        // 오버로딩의 조건
        // 1. 메서드 이름이 같아야함
        // 2. 매개변수의 개수 또는 타입이 달라야함
        // 3. 반환 타입은 영향 없음

        // A 단 이런식으로 매개변수 타입을 확실히 해줘야 나중에도 에러가 안남
        add(3L,3);
        add(3,3L);
        // add(3,3); <- 잘못된 예 (ambiguous 모호함)
        
    }
    // 이 둘은 오버로딩이 아니다 (already defined 에러)
    // int add(int x, int y){ return x+y; }
    // int add(int a, int b){ return a+b;}

    // 이 둘도 오버로딩이 아니다 반환타입은 영향 x
    // int add(int x, int y){ return x+y; }
    // long add(int a, int b){ return (long)(a+b);}

    
}
