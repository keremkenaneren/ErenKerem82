import java.util.Scanner;

public class Hesapmakinesi {
    public static void main(String[] args){
        //Kullanıcıdan veri alıcaz
        Scanner verial = new Scanner(System.in);
        
        System.out.println("1 = Toplama \n 2 = Çıkarma \n 3  = Çarpma \n 4 = Bölme \n Yapıcağınız işlemi seçin : ");
        int not = verial.nextInt();
        System.out.print("Birinci Sayı : ");
        int num1 = verial.nextInt();
        System.out.print("İkinci sayı : ");
        int num2 = verial.nextInt();
        // Koşul işlemleri
        if(not == 1){
            System.out.println(Toplama(num1,num2));
        } else if (not == 2) {
            System.out.println(cikar(num1,num2));
        } else if (not == 3) {
            System.out.println(carp(num1 , num2));
        }
        else if (not == 4){
            System.out.println(bol(num1,num2));
        }

    }
    
    // kullanıcağımız metodlar
    static int Toplama(int sayi1, int sayi2){
        int sonuc = sayi1 + sayi2;
        return sonuc;
    }
    static int cikar(int sayi1, int sayi2){
        int sonuc = sayi1 - sayi2;
        return sonuc;
    }
    static int carp(int sayi1, int sayi2){
        int sonuc = sayi1 * sayi2;
        return sonuc;
    }
    static int bol(int sayi1, int sayi2) {
        int sonuc = sayi1 / sayi2;
        return sonuc;
    }


}
