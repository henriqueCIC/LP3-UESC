import java.util.Scanner;

public class Questao1 {
    public static void main(String[] args) {
        double tot = 0;
        final double[] medida = new double[10];

        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < medida.length; i++) {
            System.out.printf("medida %d: ", i);
            double read = scanner.nextDouble();

            medida[i] = read;
            tot += read;
        }

        final double resultado = tot / medida.length;

        double varianc = 0;
        for (double v : medida)
            varianc += Math.pow(v - resultado, 2);
        varianc /= medida.length;

        // Standard deviation
        double media = Math.sqrt(varianc);

        System.out.println("Média: " + resultado);
        System.out.println("DesvPad: " + media);

        if (media > resultado * 0.1) {
            System.out.println("O multimetro está com defeito");
        } else {
            System.out.println("O multimetro está aferido corretamente");
        }
    }
}

