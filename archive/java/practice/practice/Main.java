class People implements Comparable<People>{
    String name;
    String section;
    static String department;

    static {
        department = "CS";
        System.out.println("Static Block");
    }

    public People(String name, String section) {
        this.name = name;
        this.section = section;
        System.out.println("Constructor");
    }

    public void printName() {
        System.out.printf("Name: %s", name);
    }

    public static void printDetails() {
        System.out.printf("Department: %s", department);
    }

    public void printHashCode() {
        System.out.println(this.hashCode());
    }

    @Override
    public int compareTo(People p1) {
        return (p1.name).equals(name) ? 0 : 1;
    }
}

public class Main {
    public static void main(String[] args) {
        People myObj = new People("Sinni", "A");
        myObj.printHashCode();

        myObj.name = "Singla";
        myObj.printHashCode();
    }
}
