public class Main {

    public static boolean validateStudent(String name, int age) {
        return !name.isEmpty() && age > 0;
    }

    public static void main(String[] args) {

        String studentName = "Teena";
        int studentAge = 20;

        if (validateStudent(studentName, studentAge)) {
            System.out.println("Validation Successful");
            System.out.println("Student Name: " + studentName);
            System.out.println("Student Age: " + studentAge);
        } else {
            System.out.println("Validation Failed");
        }
    }
}