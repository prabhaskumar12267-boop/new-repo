#Graded Assignment -Mini Project Report: Student Enrollment & Result Portal
#NAME-PRABHAS,ENROLLMENT NO-2502140056
student_grades = {}


# Add a new student
def add_student(name, enrollment_no, course, grade):
    student_grades[enrollment_no] = {"name": name, "course": course, "grade": grade}

    print(f"Added {name} (Enrollment No: {enrollment_no}, Course: {course}) with grade: {grade}")


# Update a student
def update_student(enrollment_no, name=None, course=None, grade=None):
    if enrollment_no in student_grades:
        if name:
            student_grades[enrollment_no]["name"] = name
        if course:
            student_grades[enrollment_no]["course"] = course
        if grade is not None:
            student_grades[enrollment_no]["grade"] = grade
        print(f"Updated record for Enrollment No: {enrollment_no}")
    else:
        print(f"Enrollment No: {enrollment_no} not found!")

# Delete a student
def delete_student(enrollment_no):
    if enrollment_no in student_grades:
        del student_grades[enrollment_no]
        print(f"Record for Enrollment No: {enrollment_no} deleted successfully.")
    else:
        print(f"Enrollment No: {enrollment_no} not found.")

# View all students
def display_all_students():
    if student_grades:
        print("\n--- Student Records ---")
        for enrollment_no, details in student_grades.items():
            print(f"Enrollment No: {enrollment_no}")
            print(f"Name: {details['name']}")
            print(f"Course: {details['course']}")
            print(f"Grade: {details['grade']}\n")
    else:
        print("No student records found.")

# Search for a student by enrollment number
def search_student(enrollment_no):
    if enrollment_no in student_grades:
        details = student_grades[enrollment_no]
        print("\n--- Student Found ---")
        print(f"Enrollment No: {enrollment_no}")
        print(f"Name: {details['name']}")
        print(f"Course: {details['course']}")
        print(f"Grade: {details['grade']}")
    else:
        print(f"No student found with Enrollment No: {enrollment_no}")
# Manage Results (Add/Update Grade only)
def manage_results(enrollment_no, grade):
    if enrollment_no in student_grades:
        student_grades[enrollment_no]["grade"] = grade
        print(f"Grade for Enrollment No: {enrollment_no} updated to {grade}")
    else:
        print(f"No student found with Enrollment No: {enrollment_no}. Please add the student first.")
# View Reports
def view_reports():
    if not student_grades:
        print("No data available to generate reports.")
        return

    print("\n--- STUDENT PERFORMANCE REPORT ---")

    total_students = len(student_grades)
    print(f"Total Students: {total_students}")

    # Extract numeric grades
    numeric_grades = []
    for details in student_grades.values():
        try:
            numeric_grades.append(float(details["grade"]))
        except ValueError:
            pass

    if numeric_grades:
        avg_grade = sum(numeric_grades) / len(numeric_grades)
        highest = max(numeric_grades)
        lowest = min(numeric_grades)

        print(f"Average Grade: {avg_grade:.2f}")
        print(f"Highest Grade: {highest}")
        print(f"Lowest Grade: {lowest}")

        # top students
        top_students = [
            (details["name"], details["grade"])
            for details in student_grades.values()
            if str(details["grade"]) == str(highest)
        ]

        print("\nTop Performers:")
        for name, grade in top_students:
            print(f"{name} - Grade: {grade}")
    else:
        print("Grades are not numeric; cannot compute averages or rankings.")




def main():
    while True:
        print("\n --------STUDENT GRADE MANAGEMENT SYSTEM--------")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Search Student")
        print("6. Manage Results(Add/Update Grade)")
        print("7. Veiw Reports")
        print("7. Exit")

        choice = int(input("Enter your choice[1,2,3,4,5,6,7]: "))

        if choice == 1:
            name = input("Enter student name: ")
            enrollment_no = input("Enter enrollment number: ")
            course = input("Enter course name: ")
            grade = input("Enter student grade: ")
            add_student(name, enrollment_no, course, grade)

        elif choice == 2:
            enrollment_no = input("Enter enrollment number to update: ")
            name = input("Enter new name (leave blank to keep unchanged): ")
            course = input("Enter new course (leave blank to keep unchanged): ")
            grade_input = input("Enter new grade (leave blank to keep unchanged): ")
            grade = (grade_input) if grade_input else None
            update_student(enrollment_no, name or None, course or None, grade)

        elif choice == 3:
            enrollment_no = input("Enter enrollment number to delete: ")
            delete_student(enrollment_no)

        elif choice == 4:
            display_all_students()
        elif choice == 5:
            enrollment_no = input("Enter enrollment number to search: ")
            search_student(enrollment_no)
        elif choice == 6:
            enrollment_no = input("Enter enrollment number to manage results: ")
            grade = input("Enter new grade: ")
            manage_results(enrollment_no, grade)
        elif choice == 7:
            view_reports()
        elif choice == 8:
            print("Closing the program...")
            break

        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
