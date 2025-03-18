package combinationExample1;

import java.util.Arrays;

public class CombineExam01 {

	static void combine(Animal[] animals, int start, int depth, Animal[] temp, int r) {
        if (depth == r) {
            System.out.println(Arrays.toString(temp));
            return;
        }

        for (int i = start; i < animals.length; i++) {
            temp[depth] = animals[i];
            combine(animals, i + 1, depth + 1, temp, r);
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

	        // 고를 동물의 수 (조합의 크기)
	        int r = 3;

	        // 조합을 담을 임시 배열
	        Animal[] temp = new Animal[r];

	        // 조합을 구하는 함수 호출 (0부터 시작, depth는 0, r은 3)
	        combine(animals, 0, 0, temp, r);
	    }
	}

