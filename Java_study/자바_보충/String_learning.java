package Java_study.자바_보충;

public class String_learning {
    public static void main(String[] args) {
//        String은 내용을 변경할 수 없는 불변(immutable) 클래스.
        String a="a";
        String b="b";
        a=a+b;
//        이렇게 더할 경우 a 주소 내용물이 바뀌는게 아니라 다른 메모리 주소에 새로운 문자열이 만들어짐
//        문자열의 변경이나 결합이 잦다면 StringBuffer 클래스를 이용


//        둘중 위엣것이 바람직함. 위엣것은 같은 것을 다른 참조변수가 이용. 아랫것은 항상 새로운 문자열이 만들어짐
//        문자열 리터럴은 프로그램 실행시 자동으로 만들어져 constant pool에 저장
        String str1="abc";
        String str2="abc";

        String str3=new String("def");
        String str4=new String("def");

//        둘이 같으면 0, 앞에것이 사전순으로 이전이면 음수, 이후면 양수
        str1.compareTo(str2);

//        문자열 합치기
        str1.concat(str3);

//        Charsequence는 인터페이스. 문자열에 관한 공통조상이 없는 클래스들이 많아서 한번에 다루기 위함
//        String.contains(CharSequence s)
        str1.contains(str2);

//        대소문자 구분 안하고 비교
        str1.equalsIgnoreCase(str3);

//        문자열에서 몇번째에 문자가 있는지. 검색 시작위치를 두번째 파라미터로 넣는것 가능
//        str1.indexOf()


//        문자열 양쪽의 공백을 없앰
        str1.trim();

//        다른 타입들의 문자열 변환. Date클래스를 넣어도 특정 양식으로 반환, int+""보다 빠름
//        String.valueOf()


//        String 배열내 문자열들사이를 구분자로 이어줌
//        String 배열.join("구분자")


//    StringBuffer는 내부에 배열을 가지고있음.
//    배열은 크기변경 불가이므로 배열보다 긴 문자열이 들어오면 새 배열 생성, 기존 문자열 복사, 참조변수 전환 3단계 필요.
//    저장할 문자열의 길이를 고려해 적절한 크기로 생성해야함. 크기를 정해주지 않으면 기본적으로 16길이. 문자열을 넣으면 문자열길이+16만큼 길이

//    StringBuffer의 equals는 오버라이딩 되어있지 않다 그러므로 String으로 변환한 다음 비교해야함



//        스트링버퍼배열의 크기
        new StringBuffer().capacity();

//        실제 담긴 문자열의 크기
        new StringBuffer().length();

//        길이 변경. 더짧아지게도 할 수 있고 그러면 뒤에건 잘림. 길게하면 뒤에 남는 공간은 null로 채워짐
        new StringBuffer().setLength(4);


//        StringBuffer는 동기화가 되어있다. 멀티쓰레드에 안전. StringBuilder 동기화가 안되어있다.
//        StringBuilder가 성능이 더 좋기 때문에 싱글쓰레드라면 굳이 StringBuffer를 쓸 이유가 없다
//        클래스의 메서드 사용법 같은 건 둘이 같다

    }

}
