package dam;

public class Palillo {

	private int numero;
	boolean enUso;
	
	public Palillo(int x) {
		numero = x;
		enUso = false;
	}
	
	public synchronized void coger() {
		while (enUso) {
			try {
				wait();
			} catch (InterruptedException e) {}
		}
		enUso = true;
		System.out.println("Palillo " + numero + " ocupado");
		notify();
	}
	
	public synchronized void soltar() {
		enUso = false;
		notify(); ///??? O vale con notifyAll()?
		System.out.println("Palillo " + numero + " se ha quedado libre");
	}
}
