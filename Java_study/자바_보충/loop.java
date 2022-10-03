package Java_study.자바_보충;

import java.util.*;
public class loop {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        sc.close();

        // do while문 형식
        do{
            System.out.println(n--);
        }while(n>0);


        // 2개 이상의 반복문 탈출: 반복문에 이름 부여

    loop: for(int i=0; i<10; i++){
        for (int j=0; j<10; j++){
            if(i==5&& j==9){
                break loop;
            }
            System.out.printf("%d %d\n",i,j);
        }
    }
    }
}
