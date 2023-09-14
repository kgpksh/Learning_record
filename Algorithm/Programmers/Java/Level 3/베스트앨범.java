import java.util.*;

class 베스트앨범 {
    Map<String, Integer> genresOrder = new HashMap();
    
    public int[] solution(String[] genres, int[] plays) {
        List<Music> musics = new ArrayList();
        
        for(int idx = 0; idx < genres.length; idx ++) {
            genresOrder.put(genres[idx], genresOrder.getOrDefault(genres[idx], 0) + plays[idx]);
            musics.add(new Music(idx, genres[idx], plays[idx]));
        }
        
        Collections.sort(musics);
        
        Map<String, Integer> countGenre = new HashMap();
        List<Integer> answer = new ArrayList();
        for(Music music : musics) {
            int count = countGenre.getOrDefault(music.genre, 0);
            if(count != 2) {
                countGenre.put(music.genre, count + 1);
                answer.add(music.index);
            }
        }
        
        int L = answer.size();
        int[] result = new int[L];
        for(int i = 0; i < L; i++) {
            result[i] = answer.get(i);
        }
        return result;
    }
    
    
    class Music implements Comparable<Music> {
        int index;
        String genre;
        int play;
        
        public Music(int index, String genre, int play) {
            this.index = index;
            this.genre = genre;
            this.play = play;
        }
        
        @Override
        public int compareTo(Music m) {
            int order = genresOrder.get(this.genre);
            int anotherOrder = genresOrder.get(m.genre);
            
            if(order - anotherOrder != 0) {
                return anotherOrder - order;
            }
            
            if(this.play - m.play != 0) {
                return m.play - this.play;
            }
            
            return this.index - m.index;
        }
    }
}