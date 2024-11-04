class CodeGradeUser:

    def __init__(self, username, institute):
        self.username = username
        self.institute = institute
    
    def hello(self):
        print(f"Hello {self.username} from {self.institute}")

class Student(CodeGradeUser):

    def __init__(self, username, institute, graduation_year):
        super().__init__(username, institute)
        self.graduation_year = graduation_year

    def graduated(self):
        if int(self.graduation_year) < 2024:
            print("True")
        else:
            print("False")
    
    def handin(self, str):
        if int(self.graduation_year) >= 2024:
            print(f"Thanks, Peter! Your submission {str} Python was successfully handed in!")
        else:
            print("Sorry Peter, you can only hand in if you haven’t graduated yet!")

class Teacher(CodeGradeUser): 

    def teach(str):
        return ("Fun fact: Python was named by Guido Van Rossum after Monty Python TV Show" )
    
    def grade(self, stud, grade):
        if self.institute == stud.institute:
            print(f"Teacher {self.username} graded {stud.username} with grade {grade}")
        else:
            print(f" You cannot grade {stud.username} as they are from another institute.")

user = CodeGradeUser("John", "Code University")
user.hello()

devin = Student("Devin", "University of Amsterdam", 2018)
devin.graduated()
devin.handin("Python Assignment")

robin = Teacher("Robin", "Code University")
robin.teach()
robin.grade(devin, 90)

peter = Student("Peter", "Code University", 2024)
peter.handin("Python Assignment")
robin.grade(peter, 85)

peter = Student("Ryan", "Code University", 2025)
robin.grade(peter, 25)

robin = Teacher("Robin", "Code University")
print(type(robin.teach()))