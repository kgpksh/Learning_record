import java.util.*;

class 게임_맵_최단거리 {
    public int solution(int[][] maps) {
        int[] moveY = {0, 0, 1, -1};
        int[] moveX = {1, -1, 0, 0};
        
        int n = maps.length;
        int m = maps[0].length;
        int[][] visited = new int[n][m];
        visited[0][0] = 1;
        
        Deque<Integer[]> deque = new LinkedList();
        Integer[] coord = {0, 0};
        deque.offer(coord);
        
        while(!deque.isEmpty()) {
            Integer[] coor = deque.pollFirst();
            int y = coor[0];
            int x = coor[1];
            for(int i = 0; i < 4; i++) {
                int nextY = y + moveY[i];
                int nextX = x + moveX[i];
                if(nextY >= 0 && nextY < n && nextX >= 0 && nextX < m && maps[nextY][nextX] == 1
                    && visited[nextY][nextX] == 0) {
                    
                    visited[nextY][nextX] = visited[y][x] + 1;
                    Integer[] next = {nextY, nextX};
                    deque.offer(next);
                }
            }
        }
        
        if(visited[n - 1][m - 1] == 0) {
                return -1;
            }
            
        return visited[n - 1][m - 1];
    }
}