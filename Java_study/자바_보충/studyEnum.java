package Java_study.자바_보충;

public class studyEnum {
    enum Kind {EAST, WEST, SOUTH, NORTH}
    enum Value {TWO, THREE, FOUR}

    public static void main(String[] args) {
//        다른 종류의 Enum 간에는 못씀
//        System.out.println(Kind.EAST == Value.TWO);

//        enum 비교 하는 법
        System.out.println(Kind.EAST == Kind.EAST);
        System.out.println(Kind.EAST.compareTo(Kind.EAST));

//        부등호는 사용 불가
//        System.out.println(Kind.EAST > Kind.SOUTH);


        System.out.println();
//        name : 열거형 상수의 이름 반환, ordinal: 열거형 상수가 정의된 순서를 반환
        System.out.println(Kind.SOUTH.name());
        System.out.println(Kind.SOUTH.ordinal());

//        values : 모든 열겨형 상수배열 반환
//        values와 valueOf는 컴파일러가 자동 추가
        for (Kind kind : Kind.values()) {
            System.out.println(kind);
        }


    }

    enum Custom {
        A(1, "A"), B(2, "b");

        private final int value;
        private final String str;

//        생성자는 항상 private임 생략되어 있을 뿐
        Custom(int value, String str) {
            this.value = value;
            this.str = str;
        }
    }
}
