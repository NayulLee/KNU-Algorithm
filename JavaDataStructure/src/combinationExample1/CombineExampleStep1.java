package combinationExample1;

import java.util.Arrays;

/* 1마리부터 7마리까지 모든 가능한 조합 출력
 * 조합은 중복 없이, 순서는 사전 순 정렬
 * 각 조합은 출력 전에 사전 순 정렬*/
public class CombineExampleStep1 {

	static String[] animals = {"사자", "호랑이", "코끼리", "기린", "늑대", "여우", "곰"};

	/* result는 조합 결과를 담는 배열
	 * start : 다음 동물을 고를 시작 위치(중복을 방지하기 위함)
	 * depth : 지금까지 몇 마리를 골랐는지(모든 가능한 조합 다 출력할것임)
	 * r : 목표로 뽑을 동물 수*/
	static void combine(String[] result, int start, int depth, int r) {
		if(depth == r) { // 목표로 3마리 뽑을건데 3마리 다뽑았으면 result배열 출력한다.
			System.out.println(Arrays.toString(result));
			return;
		}
		for(int i = start; i < animals.length; i++) { // 동물 고르기 반복문
			// 현재 위치(start)부터 animals.length(animals갯수) 까지 반복
			result[depth] = animals[i]; // result에 start인덱스 동물 한마리 넣는다.
			combine(result, i + 1, depth + 1, r);
			/* 다음 동물 고르기 위해 재귀 호출
			 * (중복 방지)다음 인덱스부터 넣어야하니까 i+1, 몇마리 뽑았는지 진행상황 depth + 1*/
		}
	}
	public static void main(String[] args) {
			Arrays.sort(animals);
			
			/*for(int r = 1; r <= animals.length; r++) {
				System.out.println("\n== " + r + "마리 조합 == ");
				combine(new String[r], 0, 0, r);*/
			
			int r = 3;
			combine(new String[r], 0, 0, r);
			}
		
	}

