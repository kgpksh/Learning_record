import java.io.*;

public class Hello_World {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("Hello World!");

        br.close();
        bw.flush();
        bw.close();
    }
}