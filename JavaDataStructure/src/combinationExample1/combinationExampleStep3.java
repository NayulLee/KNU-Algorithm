package combinationExample1;

import java.util.Arrays;

public class combinationExampleStep3 {

	static void combine(Animal[] animals, Animal[] result, int start, int step, int selectedCount, int totalWeight) {
		if(step == selectedCount) {
			if(totalWeight <= 7) {
				System.out.print(Arrays.toString(result));
				System.out.println(" --> Weight : " + totalWeight);
			}
			return;
		}

		for (int i = start; i < animals.length; i++) {
			result[step] = animals[i];
			combine(animals, result, i + 1, step + 1, selectedCount, totalWeight + result[step].weight);
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
		
		int selectedCount = 2;
		combine(animals, new Animal[selectedCount], 0, 0, selectedCount, 0);
	
	}

}
