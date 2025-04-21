package Inheritence.SubP1;

public class AdvCalculator extends Calculator {
     protected int n1;
     protected int n2;

    public AdvCalculator(int n1, int n2) {
        super(n1, n2);
        this.n1 = n1;
        this.n2 = n2;
    }

    @Override
    public int add() {
        return n1 - n2;
    }

    public static void main(String[] args) {
        Calculator calc = new AdvCalculator(1,2); // will use derived class add method
        System.out.println(calc.add());
    }
}
