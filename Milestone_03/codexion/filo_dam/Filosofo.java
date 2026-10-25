package dam;

public class Filosofo implements Runnable {

	private Thread hilo;
	private Cena cena;
	private int pizq, pder;
	private int numero;
	private int veces;
	private String color;
	
	public Filosofo(int x, int nVeces, Cena suCena, String c) {
		color = c;
		numero = x;
		cena = suCena;
		veces = nVeces;
		pizq = cena.getPalilloIzq(x);
		pder = cena.getPalilloDer(x);
		hilo = new Thread(this);
		hilo.start();
	}
	
	
	@Override
	public void run() {
		for (int i = 0 ; i < veces ; i++){
			pensar();
			cogerPalillos();
			comer();
			soltarPalillos();
		}
		System.out.println(CC.RESET + "Cena finalizada");
	}

	
	private void pensar(){
        System.out.println(color + "Filósofo " + numero + " está pensando...");
        try {
			Thread.sleep((long)(Math.random() * 2001));
		} catch (InterruptedException e) {}
    }
    
    private void comer(){
        System.out.println(color + "Filósofo " + numero + " está comiendo");
        try {
			Thread.sleep((long)(Math.random() * 2001));
		} catch (InterruptedException e) {}
        System.out.println(color + "Filósofo " + numero + " está satisfecho");
    }
    
    private void cogerPalillos(){
        System.out.println(color + "Filósofo " + numero + " intenta coger sus palillos");
        if (numero % 2 == 0) {
        	cena.getPalillo(pizq).coger();
        	cena.getPalillo(pder).coger();
        }
        else
        {
        	cena.getPalillo(pder).coger();
        	cena.getPalillo(pizq).coger();
        }
    }
    
    private void soltarPalillos(){
        System.out.println(color + "Filósofo " + numero + " suelta sus palillos");
    	cena.getPalillo(pizq).soltar();
    	cena.getPalillo(pder).soltar();
    }
}
