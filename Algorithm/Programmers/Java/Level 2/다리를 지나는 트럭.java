import java.util.Queue;
import java.util.LinkedList;

class 다리를_지나는_트럭 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int arrived = 0;
        int currentWeight = 0;
        Queue<Integer> bridge = new LinkedList<>();
        for(int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }
        
        Queue<Integer> trucks = new LinkedList<>();
        for(int i : truck_weights) {
            trucks.add(i);
        }
        
        while(arrived < truck_weights.length) {
            answer++;
            
            int outTruck = bridge.poll();
            if(outTruck != 0) {
                arrived++;
                currentWeight -= outTruck;
            }
            
            Integer startingTruck = trucks.peek();
            if(startingTruck != null && currentWeight + startingTruck <= weight) {
                bridge.add(trucks.poll());
                currentWeight += startingTruck;
            } else {
                bridge.add(0);
            }
        }
        return answer;
    }
}