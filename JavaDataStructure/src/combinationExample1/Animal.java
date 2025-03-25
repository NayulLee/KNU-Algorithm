package combinationExample1;

public class Animal {
	String name;
	int weight;
	int preference;
	
	public Animal(String name, int weight, int preference){
		this.name = name;
		this.weight = weight;
		this.preference = preference;
	}
	
	public void displayAnimalStatus() {
		System.out.println("Weight:" + weight + 
							"Preference:" + preference);
	}
	
	@Override
	public String toString() {
		return this.name;
	}
}
