class People {
    String name;
    static String department;

    static {
        department = "CS";
        System.out.println("Static Block");
    }

    public People(String name) {
        this.name = name;
        System.out.println("Constructor");
    }

    public void printName() {
        System.out.printf("Name: %s", name);
    }

    public static void printDetails() {
        System.out.printf("Department: %s", department);
    }
}
public class Main {
    public static void main(String[] args) {
        People myObj = new People("Sinni");
        myObj.printName();
        People.printDetails();
    }
}
