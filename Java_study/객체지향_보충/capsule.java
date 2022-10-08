package Java_study.객체지향_보충;

public class capsule {
}

class Time{
//    접근제어자를 쓰는 이유: 1.외부에서 데이터를 보호하기 위해  2.외부에는 불필요한 내부에서만 사용되는 부분을 감추기 위해
//    private를 통해 외부에서의 직접접근막음, 메서드를 통한 간접접근만 허용
    private int hour; //0~23만 허용
    private int minute; //0~59만 허용
    private int second; //0~59만 허용

    public int getHour() {
        return hour;
    }

//    이거도 사실 private으로 하면됨. 어차피 여기서만쓸꺼니까
    public void setHour(int hour) {
        if (hour<0 || hour>23){
            return;
        }
        this.hour = hour;
    }
}