//숫자 합을 구하자.
//N개의 숫자가 공백 없이 써져이쑈다. 이 수를 모두 합하지.

//1줄input 에는 숫자의 개수 n
//2줄input 에는 공백없이 주어진 n개의 숫자.

import java.util.Scanner;

public class Backjoon11720 {
	public static void main(String[]args) {
		
		Scanner s = new Scanner(System.in);
		//int numb = s.nextInt();
		String sNumb = s.next();
		char[] cNumb = sNumb.toCharArray();
		
		int sum = 0;
		for(int i=0; i<cNumb.length; i++) {
			System.out.println(cNumb[i]);
			sum += cNumb[i] - '0';
		}
		System.out.println(sum);
	}
}
