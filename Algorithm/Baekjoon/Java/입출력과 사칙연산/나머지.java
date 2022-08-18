import java.util.*;

public class 나머지 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        int A = Integer.parseInt(str[0]);
        int B = Integer.parseInt(str[1]);
        int C = Integer.parseInt(str[2]);

        System.out.println((A + B) % C);
        System.out.println(((A % C) + (B % C)) % C);
        System.out.println((A * B) % C);
        System.out.println(((A % C) * (B % C)) % C);
        sc.close();
    }
}
