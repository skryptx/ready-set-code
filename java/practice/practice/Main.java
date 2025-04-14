public class Main {
    public static void main(String[] args) {
        String name1 = "Sinni";
        String name2 = "Sinni";
        if(name1.equals(name2)) {
            System.out.println("equal");
        }
        System.out.format("%d, %d", System.identityHashCode(name1), System.identityHashCode(name2));
    }
}
