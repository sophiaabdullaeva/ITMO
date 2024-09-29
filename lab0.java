import java.util.Random;
public class lab0 {
	public static void main(String[] args) {
		int[] z = new int[12];
		float[] x = new float[17];
		double[][] r = new double[12][17];
		Random ran = new Random();
		int start = 4;
		for(int i = 0; i < 12; i++) {
			z[i] = start;
			start += 1;
		}
		for(int i = 0; i < 17; i++) {
			x[i] = (float) ran.nextDouble(-13, 8);
		}
		for(int i = 0; i < 12; i++) {
			for(int j = 0; j < 17; j++){
				if(z[i] == 13) {
					r[i][j] = Math.asin(Math.cos(Math.atan(Math.cos(x[j]))));
				}
				if(z[i] == 5 || z[i] == 6 || z[i] == 7 || z[i] == 8 || z[i] == 9 || z[i] == 10 || z[i] == 11) {
					r[i][j] = Math.log(Math.pow((Math.abs(x[j])/2.0), 2));
				} else {
					r[i][j] = Math.sin(Math.log(Math.pow((Math.cos(Math.pow((3.0/((1.0/3.0)-Math.atan(x[j]-2.5/21.0))),(Math.pow(x[j], (1.0/4.0)*x[j]))))), 2)));
				}
			}
		}
		for(int i = 0; i < 12; i++) {
			for(int j = 0; j < 17; j++) {
				System.out.printf("%10.5f", r[i][j]);
				System.out.print(" ");
			}
			System.out.println();
		}
	}
}


