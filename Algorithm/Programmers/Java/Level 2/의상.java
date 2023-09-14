import java.util.HashMap;
import java.util.Map;

public class 의상 {
    public int solution(String[][] clothes) {
        Map<String, Integer> maps = new HashMap();
        
        for(String[] cloth : clothes) {
            String type = cloth[1];
            maps.put(type, maps.getOrDefault(type, 0) + 1);
        }
        
        int answer = 1;
        for(int num : maps.values()) {
            answer *= (num + 1);
        }
        return answer - 1;
    }
}
