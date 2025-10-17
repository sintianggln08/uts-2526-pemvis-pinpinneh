import java.util.*;
import java.lang.Math;

public class JavaApplication {
    private static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int jumlah, rataRata, min, max, i;
        int[] nilai = new int[4];

        i = 0;
        System.out.println("Masukkan jumlah mahasiswa: ");
        jumlah = Integer.parseInt(input.nextLine());
        for (i = 0; i <= 3; i++) {
            System.out.println("Masukkan nilai: ");
            nilai[i] = Integer.parseInt(input.nextLine());
            jumlah = jumlah + nilai[i];
        }
        if (i == 0) {
            max = nilai[i];
            min = nilai[i];
        }
        rataRata = (double) jumlah / 4;
        System.out.println("Rata-Rata= " + rataRata);
        System.out.println("Tertinggi= " + max);
        System.out.println("Terendah= " + min);
    }
}
