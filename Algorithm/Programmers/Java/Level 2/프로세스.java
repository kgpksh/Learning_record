import java.util.*;

class 프로세스 {
    public int solution(int[] priorities, int location) {
        int L = priorities.length;
        
        Deque<Element> deque = new LinkedList();
        List<Integer> order = new ArrayList();
        for(int i = 0; i < L; i++) {
            order.add(priorities[i]);
            deque.add(new Element(i, priorities[i]));
        }
        
        Collections.sort(order);
        L--;
        
        int answer = 1;
        while(true) {
            Element element = deque.peekFirst();
            boolean isBiggest = order.get(L) == element.content;
            boolean isTarget = element.idx == location;
            
            if(!isBiggest) {
                deque.add(deque.pollFirst());
                continue;
            }
            
            if(isTarget) {
                return answer;
            }
            
            answer++;
            L--;
            deque.pollFirst();
        }
    }
    
    class Element {
        int idx;
        int content;
        
        public Element(int idx, int content) {
            this.idx = idx;
            this.content = content;
        }
    }
}