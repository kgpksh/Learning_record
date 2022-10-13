package Java_study.자바_보충;

public class exception_leanring {
    public static void main(String[] args) {

//        checked 예외: 컴파일러가 예외처리 확인함. 예외처리 필수 그냥 예외와 자손
//        uncehcked 예외: 컴파일러가 예외처리 확인 안함. 예외처리 선택 런타임 예외와 자손


        try{
            System.out.println(4/0);
        }catch (ArithmeticException ae){
//            ae.printStackTrace(); //예외 내용과 발생 장소 출력
        }catch (Exception e){ //모든 예외의 조상
            System.out.println("Exception");
        }


        try{
            System.out.println(6/0);

//            멀티 catch 블럭. 내용이 같은 catch 블럭을 하나로 (jdk 1.7부터)
//            굳이 부모 자식관계 둘다 쓰는건 할필요 없음
//            두 예외모두 공통된 멤버만 사용가능
        }catch (ArithmeticException | ClassCastException ae){
            ae.printStackTrace();
        }



//        고의로 예외 발생시키기
        try{
            Exception e=new Exception("직접 만든 예외 객체");

//            예외 발생
            throw e;
        }catch (Exception exception){
            System.out.println(exception.getMessage());

//            무조건 finally는 실행됨
        }finally {
            System.out.println("Finally");
        }

    }


//    예외처리를 다른데 맡김
    static void method() throws SpaceException, MemoryException {
        boolean enoughSpace=false;
        boolean MemoryException=false;
        if (!enoughSpace){
            throw new SpaceException("My SpaceException");
        }

        if (!MemoryException){
            throw new MemoryException("My MemoryException");
        }

    }

    static void install() throws InstallException{
        try{
            throw new SpaceException("Space exception");
        }catch (SpaceException e){
            InstallException ie=new InstallException("Install Exception");

//            연결된 예외, InstallException을 발생시키는 원인예외인 SpaceException
//            여러 예외를 하나로 묶어서 다룰 수 있음
            ie.initCause(e);
        }
    }

    static void startInstall() throws SpaceException{
        boolean enoughSpace=false;
        boolean enoughMemory=false;
        if (!enoughSpace){
            throw new SpaceException("설치공간 부족");
        }

//        연결된 예외를 통하여 checked 예외(MemoryException)를 unchecked 예외(RuntimeException)로 바꿔줌
        if (enoughMemory){
            throw new RuntimeException(new MemoryException("메모리 부족"));
        }
    }
}


class InstallException extends RuntimeException{
    InstallException(String msg){
        super(msg);
    }
}


//unchecked예외인 runtimeexception이나 그냥 exception을 적절히 상속해야함
class SpaceException extends RuntimeException{
    SpaceException(String msg){
        super(msg);
    }

}

class MemoryException extends Exception{
    MemoryException(String msg){
        super(msg);
    }

}

