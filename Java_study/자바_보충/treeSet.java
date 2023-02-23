package Java_study.자바_보충;

import java.util.*;

public class treeSet {
    public static void main(String[] args) {
//        TreeSet 메서드들 정리


//        기본생성자
        TreeSet treeSet1=new TreeSet();

        treeSet1.add(30);
        treeSet1.add(40);
        treeSet1.add(50);

//        주어진 컬렉션을 저장하는 TreeSet 생성
//        TreeSet treeSet2=new TreeSet(Collection c);

//        주어진 기준으로 정렬하는 TreeSet 생성
//        TreeSet treeSet3=new TreeSet(Comparator comp);


//        각각 주어진 순서에서 첫째, 마지막. 가장 작은것, 큰것
        Object first=treeSet1.first();
        Object last= treeSet1.last();

//        지정된 객체와 같은 객체를 반환. 없으면 가장 가까운 큰값을 가진객체. 그거도 없으면 null
//        Object ceiling=treeSet1.ceiling(Object o);
//        반대
//        Object flooring= treeSet1.floor(Object o);

        treeSet1.floor(35); //30반환
        treeSet1.ceiling(45); //50반환


//        위 둘은 입력된 것과 같은것은 반환안함
        treeSet1.higher(40); //50
        treeSet1.lower(40); //30


//        범위검색
        SortedSet sortedSet=treeSet1.subSet(30,40);

//        각각 지정된 객체보다 큰것과 작은것들 반환.
        SortedSet headSet=treeSet1.headSet(40);
        SortedSet tailSet=treeSet1.tailSet(40);

//        그대로 넣으면 오류. 비교기준이 없기때문.
//        TreeSet treeSet2=new TreeSet();
//        treeSet2.add(new Test());

//        다음과 같이 비교기준 넣어줘야함
        TreeSet treeSet2=new TreeSet(new TestComp());
        treeSet2.add(new Weapons());

        TreeSet stringFinder= new TreeSet();
        stringFinder.add("abc");
        stringFinder.add("bsz");
        stringFinder.add("cts");
        stringFinder.add("dzzz");
        stringFinder.add("ewd");

//        b에서 c로 시작하는 단어들만 찾는 방법
        stringFinder.subSet("b","dzzz");



    }
}

class Test{}

class TestComp implements Comparator{

    @Override
    public int compare(Object o1, Object o2) {
        return 1;
    }
}