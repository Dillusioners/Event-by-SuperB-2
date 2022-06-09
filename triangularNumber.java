import java.lang.Math;
import java.util.Scanner;

class triangularNumber {
  public static void main(String args[]){
     Scanner sc = new Scanner(System.in);
     println("##########################################################################");
     println("#   WELCOME TO THE PROGRAM TO CHECK IF A NUMBER IS A TRIANGULAR NUMBER   #");
     println("##########################################################################");
     int sum = 0;
     int triangularNumbers[] = new int[999999];
     for(int counter = 1; counter < 999; counter++){
       sum = sum + counter;
       triangularNumbers[counter] = sum;
     }
    print("Enter the number of you to check: ");
    int number = sc.nextInt();
    if(findIndex(triangularNumbers, number) != -1){
      println("The number is a triangular number.");
    }
    else{
      println("The number is not a triangular number.");
    }
    println("**************************************************************************");
  }

  static void println(String text) {
     System.out.println(text);
   }

   static void print(String text) {
     System.out.print(text);
   }

   public static int findIndex(int arr[], int t)
    {
 
        if (arr == null) {
            return -1;
        }
 
        int len = arr.length;
        int i = 0;
 
        while (i < len) {
            if (arr[i] == t) {
                return i;
            }
            else {
                i = i + 1;
            }
        }
        return -1;
    }
}