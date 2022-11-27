package newMode;
import java.util.Scanner;
public class Backjoon2018 {
	public static void main(String[]args) {
		
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		int count = 1;
		int start = 1;
		int end = 1;
		int sum = 1;
		
		while(end!=N) {
			if(sum==N) {
				count++;
				end++;
				sum+=end;
			}else if (sum>N) {
				sum-=start;
				start++;
			}else {
				end++;
				sum+=end;
			}
		}
		System.out.println(count);
		
	}

}
