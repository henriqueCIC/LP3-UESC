import java.util.List;
public class Questao2 {

    public static void main(String[] args) {
        int dado01 = roladado();
        int dado02 = roladado();
        int pontos = dado01 + dado02;

        System.out.printf("Dado01: %d, Dado02: %d\n", dado01, dado02);
        System.out.printf("pontos: %d\n", pontos);

        if (List.of(7, 11).contains(pontos)) {
            System.out.println("VOCÊ GANHOU!!!");
            return;
        }

        if (List.of(2, 3, 12).contains(pontos)) {
            System.out.println("PERDEU!!!");
            return;
        }

        System.out.println("PRÓXIMA FASE!");

        int contador = 0;
        while (true) {
            contador++;

            dado01 = roladado();
            dado02 = roladado();
          int soma = dado01 + dado02;

            System.out.printf("Dice 1: %d, Dice 2: %d\n", dado01, dado02);
            System.out.printf("Play %d: %d\n", contador, soma);

            if (soma == 7) {
                System.out.println("VOCÊ PERDEU!!!");
                return;
            }

            if (soma == pontos) {
                System.out.println("VOCÊ GANHOU!!!");
                return;
            }
        }
    }

    private static int roladado() {
        return (int) (Math.random() * 6) + 1;
    }
}

