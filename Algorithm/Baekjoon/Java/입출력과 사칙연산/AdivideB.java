import java.util.*;

public class AdivideB {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        double a = Integer.parseInt((str[0]));
        double b = Integer.parseInt((str[1]));
        System.out.println(a / b);
        sc.close();
    }
}