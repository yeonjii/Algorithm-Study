//구간 합 구하기.
//input1: 데이터수 질문수
//inptu2: 배열
//input3~: 숫자 두 개. 예를 들어 1, 3 하면 배열 1,2,3의 수를 합한 값이 output.

import java.util.Scanner;

public class Backjoon11659 {
	public static void main(String[]args) {
		Scanner s = new Scanner(System.in);
		System.out.println("input: ");
		int N = s.nextInt();
		int query_count = s.nextInt();
		
		int arr[] = new int[N];
		int arr_sum[] = new int[N+1];
		System.out.println("array: ");
		for (int i=0 ; i<N ; i++) {
			arr[i] = s.nextInt();
		}
				
		arr_sum[0] = 0; 
		arr_sum[1] = arr[0];
		for(int i=2;i<N+1;i++) {
			arr_sum[i] = arr[i-1] + arr_sum[i-1];
		}
		
		
		int id[] = new int[2];
		for(int i=0;i<query_count;i++) {
			System.out.println("query: ");
			for (int j= 0 ; j<2;j++) {
				id[j] = s.nextInt();
			}
			System.out.println( arr_sum[id[1]] - arr_sum[id[0]-1]);
		}
		
		
	}
}
