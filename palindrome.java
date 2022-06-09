import java.util.Scanner;
class test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        int c = num;
        int k = 0;
        while (num != 0) {
            k = k*10 + (num%10);
            num = num/10;
        }
        if (k == c) {
            System.out.println("Number is a palindrome");
        } else {
            System.out.println("Number is not a palindrome");
        }
    }
}
