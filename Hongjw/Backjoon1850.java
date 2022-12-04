package pack;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class Backjoon1850 {
	public static long gcd(long a, long b) {
		if(b==0) return a;
		else return gcd(b, a%b);
	}
	
	public static void main(String[]args) throws Exception{
		Scanner s = new Scanner(System.in);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		long a = s.nextLong();
		long b = s.nextLong();
		long result = gcd(a,b);
		while(result>0){
			bw.write("1");
			result--;
		}
		bw.flush();
		bw.close();
	}
}
