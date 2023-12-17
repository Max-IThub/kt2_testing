import csv


def read_grades_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        field_names = reader.fieldnames

        grades_data = [row for row in reader]

    return field_names, grades_data


def calculate_average_grade(grades_data, field_names):
    total_grades = 0
    num_students = len(grades_data)
    valid_students = 0

    for student in grades_data:
        print(f"Name: {student.get(field_names[0], 'N/A')}, {student.get(field_names[1], 'N/A')}")
        print(f"SSN: {student.get(field_names[2], 'N/A')}")
        print(
            f"Tests: {student.get(field_names[3], 'N/A')}, {student.get(field_names[4], 'N/A')}, {student.get(field_names[5], 'N/A')}, {student.get(field_names[6], 'N/A')}")

        try:
            final_grade = float(student.get(field_names[7], 'N/A').strip('"'))
            print(f"Final: {final_grade}")
            total_grades += final_grade
            valid_students += 1
        except ValueError:
            print(f"Final: N/A (Invalid value)")

        print(f"Grade: {student.get(field_names[8], 'N/A')}")
        print()

    if valid_students > 0:
        average_grade = total_grades / valid_students
        print(f"Average Final Grade: {round(average_grade, 2)}")
    else:
        print("No valid students found.")


if __name__ == "__main__":
    grades_file_path = '../Data/grades.csv' 
    field_names, grades_data = read_grades_data(grades_file_path)
    calculate_average_grade(grades_data, field_names)
