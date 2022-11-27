package newMode;
import java.util.Scanner;
import java.io.*;

public class Backjoon10986 {
	public static void main(String[]args) throws IOException{
		Scanner s = new Scanner(System.in);
		
		int N = s.nextInt();
		int M = s.nextInt();
		
		long[] S = new long[N];
		long[] C = new long[M];
		
		long answer = 0;
		
		S[0] = s.nextInt();
		for(int i=0;i<N;i++) {
			S[i] = S[i-1] + s.nextInt();
		}
		for(int i=0;i<N;i++) {
			int re = (int)(S[i]%M);
			if (re ==0) answer++;
			C[re]++;
		}
		for(int i=0;i<M;i++) {
			if(C[i]>1)
				answer = answer+(C[i]*(C[i]-1)/2);
		}
		
		System.out.println(answer);
	}
	
}
