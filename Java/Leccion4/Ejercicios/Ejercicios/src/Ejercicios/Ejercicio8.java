/*
 Ejercicio 8: Perdir un numero N, y mostrar todos los
 numeros del 1 al N.
 */
package Ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio8 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String entradas = JOptionPane.showInputDialog("Ingrese un numero N:");
        int numero = Integer.parseInt(entradas);
        System.out.print("Tambien ingresa el mismo numero por consola: ");
        int numero2 = entrada.nextInt();  // <-- cambiar 'sc' por 'entrada'
        System.out.println("Con JOptionPane: del 1 al " + numero);
        for (int i = 1; i <= numero; i++) System.out.print(i + " ");
        System.out.println("\nCon Scanner: del 1 al " + numero2);
        for (int i = 1; i <= numero2; i++) System.out.print(i + " ");
        JOptionPane.showMessageDialog(null, "Finalizado");
        entrada.close();
    }
}