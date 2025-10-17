import java.util.*;
import java.lang.Math;

public class fibonacci_sum {
    private static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int n, jumlahderet, hasil, i;

        n = Integer.parseInt(input.nextLine());
        for (i = 1; i <= n; i++) {
            jumlahderet = 1 + 1 + 2 + 3 + n;
            hasil = jumlahderet;
        }
        System.out.println(Integer.toString(hasil) + "//" + "1+1+2+3+" + n + "");
    }
}
