package combinationExample1;

import java.util.Arrays;

public class CombinationExampleStep2 {

	static void combine(Animal[] animals, Animal[] result, int start, int step, int selectedCount) {
		if(step == selectedCount) {
			System.out.println(Arrays.toString(result));
			return;
		}
		/* result 배열은 step위치에 동물을 넣는다.
		 * step은 현재까지 고른 동물의 개수이고 i는 animals에서 동물을 고를 인덱스 번호이다.*/
		for(int i = start; i <animals.length; i++) {
			result[step] = animals[i];
			combine(animals, result, i + 1, step + 1, selectedCount);
			}
	}
	public static void main(String[] args) {
		Animal[] animals = {
				new Animal("코끼리", 6, 5),
	            new Animal("코뿔소", 3, 4),
	            new Animal("기린", 5, 4),
	            new Animal("하마", 4, 3),
	            new Animal("호랑이", 2, 1),
	            new Animal("사자", 2, 1),
	            new Animal("얼룩말", 2, 1)
		};
		
		int selectedCount = 3;
		combine(animals, new Animal[selectedCount], 0, 0, selectedCount);
	}

}
