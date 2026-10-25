package dam;

public class Cena {
	
	Palillo palillos[];
	int comensales;
	
	public Cena(int comensales) {
		palillos = (comensales > 1) ? new Palillo[comensales]: new Palillo [2];
		
		this.comensales = comensales;
		for (int i = 0 ; i < palillos.length ; i++) {
			palillos[i] = new Palillo(i);
		}
	}
	
	public Palillo getPalillo(int x) {
		return palillos[x];
	}
	
	public int getPalilloDer(int x) {
		return (comensales > 1) ? (x + 1) % comensales : 1;
	}
	
	public int getPalilloIzq(int x) {
		return x;
	}
}
