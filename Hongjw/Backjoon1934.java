package pack;
import java.util.Scanner;

public class Backjoon1934 {
	public static int gcd(int a, int b) {
		if (b==0)
			return a;
		else
			return b;
	}
	
	public static void main(String[]args) {
		Scanner s = new Scanner(System.in);
		int t = s.nextInt();
		for (int i=0;i<t;i++) {
			int a = s.nextInt();
			int b = s.nextInt();
			int result = a*b/gcd(a,b);
			System.out.println(result);
		}	
	}
}
