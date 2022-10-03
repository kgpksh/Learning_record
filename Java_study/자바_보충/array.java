package Java_study.자바_보충;

import java.lang.reflect.Array;
import java.util.Arrays;

public class array {
    public static void main(String[] args) {
        // 정수 배열은 0으로 초기화됨
        int[] arr=new int[5];

        //빠른 초기화:
        int[] array=new int[]{2,3,5,6,7};
        //혹은
        int[] array2={2,3,4,6,7};

        /*int[] array
         * array={2,45,7,8,21}
         * 이런식으로는 불가능
         */

        // 문자배열만 바로 출력가능
         char[] c={'1','d','s'};
         System.out.println(c);

        //  for문 쓰지않고 배열출력법
         System.out.println(Arrays.toString(array));

        //  배열 섞기
        for(int i=0; i<100; i++){
            int n=(int)(Math.random()*array.length);
            int tmp=array[0];
            array[0]=array[n];
            array[n]=tmp;
        }
        System.out.println(Arrays.toString(array));

        // 2차원 배열 for문 쓰지 않고 출력법
        int[][] arr2d={{1,2,3},{6,8,9}};
        int[][] arr2d2={{1,2,3},{6,8,9}};
        System.out.println(Arrays.deepToString(arr2d));

        // 두 배열 비교
        // 1차원배열 비교
        Arrays.equals(arr, array);

        // 2차원 배열배교
        Arrays.deepEquals(arr2d, arr2d2);


        // 배열 복사
        // 처음부터 2번째 매개변수의 인덱스전까지
        int[] copied=Arrays.copyOf(array, array.length);
        // 배열 범위복사
        int[] copied2=Arrays.copyOfRange(array,2,3);

        //메인메소드의 args 사용가능 입력 받을때 큰따옴표로 묶으면 띄어쓰기도 하나로 받음
    }
}
