package Algorithm.Baekjoon.Java.기본_수학_1;

import java.io.*;
import java.math.BigInteger;

public class 큰_수_AplusB {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] strs = br.readLine().split(" ");
        BigInteger a = new BigInteger(strs[0]);
        BigInteger b = new BigInteger(strs[1]);
        bw.write(a.add(b).toString());

        br.close();
        bw.flush();
        bw.close();
    }
}
