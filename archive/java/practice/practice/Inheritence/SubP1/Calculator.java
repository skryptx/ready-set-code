package Inheritence.SubP1;

public class Calculator {
    private final int n1;
    private final int n2;

    public Calculator(int n1, int n2) {
        this.n1 = n1;
        this.n2 = n2;
    }

    public int add() {
        return n1 + n2;
    }
}

