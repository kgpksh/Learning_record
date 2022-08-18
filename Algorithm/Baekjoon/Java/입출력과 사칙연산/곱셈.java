import java.util.*;

public class 곱셈 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a = Integer.parseInt(sc.nextLine());
        String s = sc.nextLine();
        char[] c = s.toCharArray();

        for (int i = 2; i > -1; i--) {
            int b = Character.getNumericValue(c[i]);
            System.out.println(a * b);
        }

        int after = Integer.parseInt(s);
        System.out.println(a * after);
        sc.close();
    }
}
