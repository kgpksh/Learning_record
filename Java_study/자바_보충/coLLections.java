package Java_study.자바_보충;

import java.lang.reflect.Array;
import java.util.*;

public class coLLections {
    public static void main(String[] args) {
        //    Collection 인터페이스에는 기본적인 메서드들이 있다  add, addAll, remove, removeAll, contains, containsAll,size 등
        
//        ArrayList는 Vector와 달리 동기화 X, 객체의 저장공간으로 배열 사용
        List list=new ArrayList<>();
        list.add(4);
        list.add(5);
        list.add(7);

//        list=[4,5,7]
        list.get(0);
        list.indexOf(4);
        list.lastIndexOf(4);
        list.set(0,4);
//        list.sort(Comparator c);
        list.subList(0,1);

//        어떤 원소를 집어서 삭제할때 방법
        list.remove(new Integer(5));
        System.out.println(list); // [4,7]
//        잘못된 방법. 원소가 아니라 Index임
//        list.remove(5);

//        ArrayList는 remove 메서드 사용시 뒤쪽 원소들 한칸씩 앞으로 복사, 마지막 원소를 null로 바꿈.
//        반복문으로 ArrayList 삭제할때는 뒤 인덱스부터 제거


        List lList=new LinkedList();
//        일반 배열은 접근시간이 짧은 장점
//        크기를 변경할 수 없어 새로운 배열을 생성후 복사해야함. 크기변경을 피하기 위해 여유로운 크기의 배열을 생성할 경우 메모리낭비
//        비순차적인 데이터의 추가, 삭제에 시간 많이 걸림.그러나 끝부분의 추가와 삭제는 빠르다
//        LinkedList는 불연속적으로 존재하는 데이터를 연결 유연한 추가,삭제, 대신 접근성이 나쁨

        Stack stk=new Stack();

//        큐는 인터페이스이다
        Queue que = new LinkedList();


//        Iterator, Enumeration 은 사실상 같다. 컬렉션에 저장된 데이터를 접근하는데 필요한 인터페이스
//        컬렉션들의 여로 종류에 저장된 요소들을 읽어오는 방법을 표준화한것
//        ListIterator는 next 뿐만아니라 previous도 있다
//        Iterator는 일회용이기 때문에 처음부터 다시 읽으려면 새로 만들어야함


//        HashSet에 뭔가를 넣기 전에 equals와 hashcode를 오버라이딩 해야 바르게 동작.
        Set set=new HashSet();
        set.addAll(list); //합집합
        set.containsAll(list); //부분집합
        set.removeAll(list); // 차집합
        set.retainAll(list); // 교집합



//        Map에는 Iterator가 없다. Collection의 자손이 아님
        Map map=new HashMap();
        map.clear();
        map.put(3,4);
        map.put(5,7);
        map.containsKey(4);
        map.containsValue(4);
        Set ets=map.entrySet(); //key-value 쌍
        Set key=map.keySet(); //key만
        map.values(); //value만

//        Map에서 Iterator를 쓰는방법
        Iterator eit=ets.iterator();
        System.out.println(ets);
        System.out.println(key);
        System.out.println(map.values());




        List lst= Arrays.asList(new Integer[]{1,2,3,4,5});
//        위에와 같음
//        List lst=Arrays.asList(1,2,3,4,5);

//        위 둘은 읽기전용이라 lst.add(6) 이런거 안됨
//        할려면
//        List list=new ArrayList(Arrays.asList(1,2,3,4,5));
//        이런 식으로


//        동기화된 자료구조를 위한 Collections의 메서드들
        List synclist=Collections.synchronizedList(new ArrayList<>());

//        읽기전용 변경불가
        List unmodilist=Collections.unmodifiableList(new ArrayList<>());


//        객체 1개만 저장할 수 있는 컬렉션
//        List singleton=Collections.singletonList(Object o);


//        한 종류의 객체만 저장하는 컬렉션. ex) String 만 저장가능
        List arrlist=new ArrayList();
        List  checked=Collections.checkedList(arrlist,String.class);


//        2로 5만큼 길이의 배열을 채움. 단 결과는 변경불가.
        List newList=Collections.nCopies(5,2);
    }
}
