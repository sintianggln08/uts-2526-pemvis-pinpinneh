import java.util.*;
import java.lang.Math;

public class JavaApplication {
    private static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int a, b, hasil, penjumlahan, pengurangan, perkalian, pembagian, pilihan;

        System.out.println("Masukkan nilai a= ");
        a = Integer.parseInt(input.nextLine());
        System.out.println("masukkan nilai b= ");
        b = Integer.parseInt(input.nextLine());
        System.out.println("menu: 1.+ 2.- 3.* 4./");
        pilihan = Integer.parseInt(input.nextLine());
        if (pilihan == 1) {
            penjumlahan = a + b;
            System.out.println(penjumlahan);
        } else {
            if (pilihan == 2) {
                pengurangan = a - b;
                System.out.println(pengurangan);
            } else {
                if (pilihan == 3) {
                    perkalian = a * b;
                    System.out.println(perkalian);
                } else {
                    if (pilihan == 4) {
                        pembagian = (double) a / b;
                        System.out.println(pembagian);
                    }
                }
            }
        }
    }
}
