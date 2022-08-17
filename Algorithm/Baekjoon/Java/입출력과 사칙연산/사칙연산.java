import java.util.*;

public class 사칙연산 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        int a = Integer.parseInt(str[0]);
        int b = Integer.parseInt(str[1]);
        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b);
        System.out.println(a % b);
        sc.close();
    }
}