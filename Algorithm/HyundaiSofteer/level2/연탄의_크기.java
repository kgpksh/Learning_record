import java.io.*;
import java.util.*;

public class 연탄의_크기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> houses = new ArrayList(n);
        while(st.hasMoreTokens()) {
            houses.add(Integer.parseInt(st.nextToken()));
        }
        
        Collections.sort(houses);
        int max = houses.get(n - 1);
        int answer = 0;
        
        for(int r = 2; r <= max; r++) {
            int count = 0;
            for(int furnace : houses) {
                if(furnace % r == 0) {
                    count += 1;
                }
            }
            answer = Math.max(count, answer);
        }

        System.out.println(answer);
    }
}
