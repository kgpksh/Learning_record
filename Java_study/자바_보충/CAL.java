package Java_study.자바_보충;

import java.time.Year;
import java.util.Calendar;
import java.util.Date;

public class CAL {
    public static void main(String[] args) {
//        Date는 자바 처음 출시때부터, Calendar는 그 이후, 그다음 1.8부터 Time패키지가 나옴
        Calendar calendar=Calendar.getInstance();
//        그달의 마지막날
        System.out.println(calendar.getActualMaximum(Calendar.DATE));

//        캘린더의 set 메서드로 특정 날짜 지정가능. 월(Month)는 0부터 시작하는 것에 주의
        calendar.set(Calendar.YEAR,2022);
        calendar.set(Calendar.MONTH, 10);
        calendar.set(Calendar.DATE, 19);
        System.out.println(calendar.getActualMaximum(Calendar.DATE));

//        캘린더 객체의 모든 필드를 초기화, 1970년 1원 1일로.
        calendar.clear();

//        add메서드는 숫자만큼 연월일등을 더함
        calendar.add(Calendar.YEAR,2);
        System.out.println(calendar.get(Calendar.YEAR)+" "+calendar.get(Calendar.MONTH)+" "+calendar.get(Calendar.DATE));

//        roll메서드는 숫자만큼 연월일등을 더하지만다른 요소에 영향을안미침 ex) 일을 더해도 달이 넘어가지 않음
        calendar.roll(Calendar.DATE,35);
        System.out.println(calendar.get(Calendar.YEAR)+" "+calendar.get(Calendar.MONTH)+" "+calendar.get(Calendar.DATE));


//        Calendar 와 Date 상호 변경법

//        Cal -> Date
        Calendar calendar2=Calendar.getInstance();
        Date d=new Date(calendar2.getTimeInMillis());

//        Date -> Cal
        Date date=new Date();
        Calendar calendar3=Calendar.getInstance();
        calendar3.setTime(date);
    }
}
