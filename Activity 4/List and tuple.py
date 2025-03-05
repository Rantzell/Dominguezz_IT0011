import pickle


def calculate_grade(class_standing, major_exam_grade):
    return 0.6 * class_standing + 0.4 * major_exam_grade


class StudentRecordManager:
    def __init__(self):
        self.records = []  

   
    def open_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.records = pickle.load(file)
            print("File loaded successfully.")
        except Exception as e:
            print(f"Error loading file: {e}")

  
    def save_file(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.records, file)
            print("File saved successfully.")
        except Exception as e:
            print(f"Error saving file: {e}")

  
    def save_as_file(self, filename):
        self.save_file(filename)

  
    def show_all(self):
        if not self.records:
            print("No student records found.")
        else:
            for record in self.records:
                student_id, name, class_standing, major_exam_grade = record
                grade = calculate_grade(class_standing, major_exam_grade)
                print(f"ID: {student_id}, Name: {name[0]} {name[1]}, Class Standing: {class_standing}, Major Exam Grade: {major_exam_grade}, Grade: {grade:.2f}")

 
    def order_by_last_name(self):
        sorted_records = sorted(self.records, key=lambda record: record[1][1])  # Sort by last name
        for record in sorted_records:
            student_id, name, class_standing, major_exam_grade = record
            grade = calculate_grade(class_standing, major_exam_grade)
            print(f"ID: {student_id}, Name: {name[0]} {name[1]}, Class Standing: {class_standing}, Major Exam Grade: {major_exam_grade}, Grade: {grade:.2f}")

 
    def order_by_grade(self):
        sorted_records = sorted(self.records, key=lambda record: calculate_grade(record[2], record[3]), reverse=True)  # Sort by grade
        for record in sorted_records:
            student_id, name, class_standing, major_exam_grade = record
            grade = calculate_grade(class_standing, major_exam_grade)
            print(f"ID: {student_id}, Name: {name[0]} {name[1]}, Class Standing: {class_standing}, Major Exam Grade: {major_exam_grade}, Grade: {grade:.2f}")

    
    def add_record(self):
        try:
            student_id = int(input("Enter Student ID (6-digit number): "))
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = int(input("Enter Class Standing (0-100): "))
            major_exam_grade = int(input("Enter Major Exam Grade (0-100): "))
            self.records.append((student_id, (first_name, last_name), class_standing, major_exam_grade))
            print("Record added successfully.")
        except ValueError:
            print("Invalid input. Please enter correct data types.")

    def edit_record(self):
        student_id = int(input("Enter Student ID to edit: "))
        record = next((r for r in self.records if r[0] == student_id), None)
        if record:
            index = self.records.index(record)
            first_name = input(f"Enter new First Name (current: {record[1][0]}): ")
            last_name = input(f"Enter new Last Name (current: {record[1][1]}): ")
            class_standing = int(input(f"Enter new Class Standing (current: {record[2]}): "))
            major_exam_grade = int(input(f"Enter new Major Exam Grade (current: {record[3]}): "))
            self.records[index] = (student_id, (first_name, last_name), class_standing, major_exam_grade)
            print("Record updated successfully.")
        else:
            print("Record not found.")

   
    def delete_record(self):
        student_id = int(input("Enter Student ID to delete: "))
        record = next((r for r in self.records if r[0] == student_id), None)
        if record:
            self.records.remove(record)
            print("Record deleted successfully.")
        else:
            print("Record not found.")


def main():
    manager = StudentRecordManager()
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Add Record")
        print("8. Edit Record")
        print("9. Delete Record")
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            filename = input("Enter file name to open: ")
            manager.open_file(filename)
        elif choice == '2':
            filename = input("Enter file name to save: ")
            manager.save_file(filename)
        elif choice == '3':
            filename = input("Enter new file name to save as: ")
            manager.save_as_file(filename)
        elif choice == '4':
            manager.show_all()
        elif choice == '5':
            manager.order_by_last_name()
        elif choice == '6':
            manager.order_by_grade()
        elif choice == '7':
            manager.add_record()
        elif choice == '8':
            manager.edit_record()
        elif choice == '9':
            manager.delete_record()
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
