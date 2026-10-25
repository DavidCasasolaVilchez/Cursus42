package dam;

public class Lanzador {

	public static void main(String[] args) {
		System.out.println("Cena de los filósofos");
		int comensales = Integer.parseInt(args[0]);
		int almuerzos = Integer.parseInt(args[1]);
		
		String[] colores = {
				CC.RED,
				CC.GREEN,
				CC.YELLOW,
				CC.BLUE,
				CC.PURPLE,
				CC.CYAN
			};
		
		var cena = new Cena(comensales);
		for (int i = 0 ; i < comensales ; i++) {
			new Filosofo(i, almuerzos, cena, colores[i]);
		}
	}
}
