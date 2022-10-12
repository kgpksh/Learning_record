package Java_study.객체지향_보충;

public class anonymous_class {
    public static void main(String[] args) {
//        익명클래스는 조상이름을 바로 new로 쓴다
        new anonymous_ancestor(){
//            --내용 구현--
        };
    }

}

class anonymous_ancestor{}