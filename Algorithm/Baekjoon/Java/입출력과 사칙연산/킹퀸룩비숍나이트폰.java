import java.util.*;

public class 킹퀸룩비숍나이트폰 {
    public static void main(String args[]) {
        int[] correct = { 1, 1, 2, 2, 2, 8 };
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        for (int i = 0; i < 6; i++) {
            System.out.print(correct[i] - Integer.parseInt(input[i]));
            if (i != 5) {
                System.out.print(" ");
            }
        }
        sc.close();
    }
}
