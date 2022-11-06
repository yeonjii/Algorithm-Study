//백준 1546
//평균 구하기

//세준은 기말고사를 망쳐 성적을 조작했다. 자기 점수의 최댓값 M에 대해 모든 점수를 점수/M*100으로 고쳤다. 이 새로운 점수의 평균은?

//input1: 성걱 개수
//ipnut2: 각 과목 성적 n개.

//풀이: 모든 점수에게 가하는 동일한 변환은 평균에게도 동일하게 적용되므로 총 기존 평균/M*100으로 새로운 평균을 구한다.

import java.util.Scanner;

public class Backjoon1546 {
	public static void main(String[]args) {
	
		Scanner s = new Scanner(System.in);
		System.out.print("input : ");
		int count = s.nextInt();
		
		System.out.print("your scores: ");
		int arr[] = new int[count];
		int sum = 0;
		for(int i=0;i<count;i++) {
			arr[i] = s.nextInt();
			sum += arr[i];
		}
		
		int max = arr[0];
		for(int i=1;i<count;i++) {
			if(max<arr[i])
			max = arr[i];
		}
		
		double result = sum*100/max/count;
		System.out.println(sum);
		System.out.println(result);
		
	}
}
