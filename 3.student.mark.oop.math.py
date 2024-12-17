import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.credits = {}
        self.gpa = 0.0

    def add_mark(self, subject, mark, credit):
        self.marks[subject] = math.floor(mark * 10) / 10 
        self.credits[subject] = credit

    def calculate_gpa(self):
        if self.marks:
            marks = np.array(list(self.marks.values()))
            credits = np.array(list(self.credits.values()))
            self.gpa = np.sum(marks * credits) / np.sum(credits) if np.sum(credits) > 0 else 0.0

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, dob):
        self.students[student_id] = Student(student_id, name, dob)

    def get_student(self, student_id):
        return self.students.get(student_id)

    def list_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr("List of Students:\n")
        for student in self.students.values():
            stdscr.addstr(f"ID: {student.student_id}, Name: {student.name}, DOB: {student.dob}, GPA: {student.gpa:.2f}\n")
        stdscr.addstr("Press any key to continue...")
        stdscr.getch()

    def sort_students_by_gpa(self):
        for student in self.students.values():
            student.calculate_gpa()
        self.students = dict(sorted(self.students.items(), key=lambda x: x[1].gpa, reverse=True))

def main(stdscr):
    manager = StudentManager()

    while True:
        stdscr.clear()
        stdscr.addstr("1. Add Student\n")
        stdscr.addstr("2. Add Mark\n")
        stdscr.addstr("3. List Students\n")
        stdscr.addstr("4. Calculate and Sort GPA\n")
        stdscr.addstr("5. Exit\n")
        stdscr.addstr("Choose an option: ")
        choice = stdscr.getstr().decode("utf-8")

        if choice == '1':
            stdscr.addstr("Enter student ID: ")
            student_id = stdscr.getstr().decode("utf-8")
            stdscr.addstr("Enter student name: ")
            name = stdscr.getstr().decode("utf-8")
            stdscr.addstr("Enter date of birth (YYYY-MM-DD): ")
            dob = stdscr.getstr().decode("utf-8")
            manager.add_student(student_id, name, dob)
            stdscr.addstr("Student added successfully!")
            stdscr.getch()

        elif choice == '2':
            stdscr.addstr("Enter student ID: ")
            student_id = stdscr.getstr().decode("utf-8")
            student = manager.get_student(student_id)

            if student:
                stdscr.addstr("Enter subject: ")
                subject = stdscr.getstr().decode("utf-8")
                stdscr.addstr("Enter mark: ")
                mark = float(stdscr.getstr().decode("utf-8"))
                stdscr.addstr("Enter credit: ")
                credit = int(stdscr.getstr().decode("utf-8"))
                student.add_mark(subject, mark, credit)
                stdscr.addstr("Mark added successfully!")
            else:
                stdscr.addstr("Student ID not found!")
            stdscr.getch()

        elif choice == '3':
            manager.list_students(stdscr)

        elif choice == '4':
            manager.sort_students_by_gpa()
            stdscr.addstr("GPAs calculated and students sorted by GPA!")
            stdscr.getch()

        elif choice == '5':
            break

        else:
            stdscr.addstr("Invalid choice! Try again.")
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)