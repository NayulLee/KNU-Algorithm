package combinationExample1;

import java.util.Arrays;

public class CombineExam01 {
	
	static int maxPreference = 0;
	
	static void combine(Animal[] animals, int start, int depth, Animal[] temp,int weightSum, int preferenceSum, int r) {
        if (depth == r) {
            // 무게가 7을 넘으면 해당 조합은 탐색하지 않는다.
        	if(weightSum <= 7) {
        		// 무게가 7 이하일 때 선호도 합을 계산하고 최대 선호도 갱신
        		maxPreference = Math.max(maxPreference, preferenceSum);
        		System.out.println(Arrays.toString(temp) + " -> 선호도 합 : " + preferenceSum);
        	}
        	return;
        }

        for (int i = start; i < animals.length; i++) {
            temp[depth] = animals[i];
            combine(animals, i + 1, depth + 1, temp, weightSum + animals[i].weight, preferenceSum + animals[i].preference, r);
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
	        for(int r = 1; r < animals.length; r++) {
	        	Animal[] temp = new Animal[r];
	        	
	        	combine(animals, 0, 0, temp, 0, 0, r);
	        }
	    }
	}

