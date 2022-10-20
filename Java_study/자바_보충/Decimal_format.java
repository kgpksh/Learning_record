package Java_study.자바_보충;

import java.text.DateFormat;
import java.text.DecimalFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Decimal_format {
//    SimpleDataFormat <- 숫자나 문자등을 특정한 형식을 바꿔주는 형식화클래스
    public static void main(String[] args) {
        double number=1234567.89;
        DecimalFormat df=new DecimalFormat("#.#E0");
        String result=df.format(number);
        System.out.println(result);


//        날짜 -> 문자열
        Date today = new Date();
        SimpleDateFormat simpleDateFormat=new SimpleDateFormat("yyyy-MM-dd");
        String day=simpleDateFormat.format(today);

//        문자열에서 날짜 뽑아내기
        DateFormat df2=new SimpleDateFormat("yyyy년 MM월 dd일");
        DateFormat df3=new SimpleDateFormat("yyyy/MM/dd");

        try {
            Date d = df2.parse("2026년 11월 14일");
            System.out.println(df3.format(d));
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }
//        열정 있는 사람들이 올 것이란 기대도 있고 개발 관련 잡담을 할 수 있을 것 같은 환경도 중요하다.

    }
}
