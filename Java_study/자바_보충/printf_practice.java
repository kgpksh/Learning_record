package Java_study.자바_보충;

public class printf_practice {
    public static void main(String[] args) {
        // 정수 출력
        // 10진
        System.out.printf("%d\n",10);
        // 8진
        System.out.printf("%o\n",10);
        // 16진
        System.out.printf("%x\n",10);

        // 접두사 붙이기, 대문자 소문자도 따라감
        System.out.printf("%#X\n",10);


        // 실수 출력
        // 소수점 이하 출력 자릿수 정하기
        System.out.printf("%.2f\n",10.0/3);
        // 지수표현식으로 출력
        System.out.printf("%e\n",10.0/3);
        // 지시자 g는 둘중 간략한 방법으로 출력

        // 문자열로 출력
        System.out.printf("%s\n",10.0/3);
        // 문자로 출력
        System.out.printf("%c\n",1);
        // 불리언으로 출력
        System.out.printf("%b\n",1);

        // 지시자 앞에 숫자를 적으면 그만큼의 공간 확보
        // 양수는 오른쪽정렬 음수는 왼쪽정렬, 길이보다 작으면 부분출력 가능
        System.out.printf("%20s\n",10.0/3);


        // 응용
        System.out.printf("age: %d year: %d\n",14,2017);

        // 이진 변환
        System.out.println(Integer.toBinaryString(15));
        
    }
}
