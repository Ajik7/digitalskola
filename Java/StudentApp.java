class Academician{
  
    String name;
    String age;
    public Academician(String name, String age){
        this.name=name;
        this.age=age;
    }
    public void studentSubject(String subject){
        System.out.println(name);
        System.out.println(age);
        System.out.println(subject);
    }
};

class Student extends Academician{
    String grade;

    public Student(String name, String age) {
        super(name, age);
        //TODO Auto-generated constructor stub
    }
   
    public void studentSubject(String subject){
        System.out.println("I am a student");
        System.out.println(name);
        System.out.println(age);
        System.out.println(subject);
    }
};

class StudentApp{
      public static void main(String[] args) {
        Student student = new Student("Aji Kurniawan","21");
        student.studentSubject("Matematika");
        }
}

