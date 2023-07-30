def add_student(student_data):
    roll_number = input("Enter the Roll Number: ")
    name = input("Enter the Name: ")
    age = int(input("Enter the Age: "))
    grade = input("Enter the Grade: ")

    student_data[roll_number] = {
        "Name": name,
        "Age": age,
        "Grade": grade
    }
    print("Student added successfully!")


def view_students(student_data):
    if not student_data:
        print("No students found.")
    else:
        print("Student Records:")
        for roll_number, student_info in student_data.items():
            print(f"Roll Number: {roll_number}")
            for key, value in student_info.items():
                print(f"{key}: {value}")
            print()


def delete_student(student_data):
    roll_number = input("Enter the Roll Number of the student to delete: ")

    if roll_number in student_data:
        del student_data[roll_number]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def main():
    student_data = {}  # Dictionary to store student records

    while True:
        print("\n--- School Administration Program ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_student(student_data)
        elif choice == "2":
            view_students(student_data)
        elif choice == "3":
            delete_student(student_data)
        elif choice == "4":
            print("Exiting School Administration Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
