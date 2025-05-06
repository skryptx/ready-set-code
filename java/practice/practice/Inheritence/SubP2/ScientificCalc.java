package Inheritence.SubP2;

import Inheritence.SubP1.AdvCalculator;

public class ScientificCalc extends AdvCalculator {
    public ScientificCalc(int n1, int n2) {
        super(n1, n2);
    }

    public int divide() {
        return n1/n2;
    }

    public static void main(String[] args) {
        System.out.println(new ScientificCalc(132,66).divide());
        System.out.println(new ScientificCalc(4,5).add());
    }
}
