package Java_study.자바_보충;

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


        Set set=new HashSet();
        set.addAll(list); //합집합
        set.containsAll(list); //부분집합
        set.removeAll(list); // 차집합
        set.retainAll(list); // 교집합



        Map map=new HashMap();
        map.clear();
        map.put(3,4);
        map.put(5,7);
        map.containsKey(4);
        map.containsValue(4);
        Set ets=map.entrySet(); //key-value 쌍
        Set key=map.keySet(); //key만
        map.values(); //value만
        System.out.println(ets);
        System.out.println(key);
        System.out.println(map.values());
    }
}
