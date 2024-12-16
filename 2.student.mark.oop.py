class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def list_marks(self):
        if self.marks:
            print(f"\nMarks for {self.name}:")
            for subject, mark in self.marks.items():
                print(f"Subject: {subject}, Mark: {mark}")
        else:
            print("No marks available for this student.")

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, dob):
        self.students[student_id] = Student(student_id, name, dob)

    def get_student(self, student_id):
        return self.students.get(student_id, None)

    def list_students(self):
        print("\nStudents:")
        for student in self.students.values():
            print(f"ID: {student.student_id}, Name: {student.name}, DOB: {student.dob}")

def main():
    manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. Add Mark")
        print("3. List Students")
        print("4. List Marks")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            manager.add_student(student_id, name, dob)
            print("Student added successfully.")

        elif choice == '2':
            student_id = input("Enter student ID: ")
            student = manager.get_student(student_id)
            if student:
                subject = input("Enter subject: ")
                mark = float(input("Enter mark: "))
                student.add_mark(subject, mark)
                print("Mark added successfully.")
            else:
                print("Student ID not found.")

        elif choice == '3':
            manager.list_students()

        elif choice == '4':
            student_id = input("Enter student ID: ")
            student = manager.get_student(student_id)
            if student:
                student.list_marks()
            else:
                print("Student ID not found.")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()