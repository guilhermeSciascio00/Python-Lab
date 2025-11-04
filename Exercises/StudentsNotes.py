#A simple program that will get the average of the students, who has the higher/lower score, and the user can also update it

def average_calc(numbers : list[float]) -> float:        
    return round(sum(numbers) / len(numbers), 2)
    
def add_new_student(student_name : str, student_grade : int) -> None:
    class_students[student_name] = student_grade
    

def get_student_by_grade(grade : float) -> str:
    for student, student_grade in class_students.items():
        if student_grade == grade:
            return student 

def display_student_names_grades() -> None:
    print()
    for student in class_students.keys():   
        print(f"{student} => {class_students[student]}")
    print()

def display_highest_lowest_grades() -> None:
    print(f"Highest Grade in Class: {get_student_by_grade(max(class_students.values()))} -> {max(class_students.values())}")
    
    print(f"Lowest Grade in Class: {get_student_by_grade(min(class_students.values()))} -> {min(class_students.values())}")

def display_class_average() -> None:
    print(f"Class average: {average_calc([grade for grade in class_students.values()])}")

class_students : dict = {"Alice" : 85.0, "Bob" : 92.0, "Wallace" : 75.0}

print("\nWelcome to the class room!")
print("Here are our students and their grades: ")

display_student_names_grades()
display_class_average()
display_highest_lowest_grades()


print("Please, add a new student: ") 
student_name = input("Name: ").capitalize()
student_grade = float(input("Grade: "))

add_new_student(student_name, student_grade)

option = input("Press anything to continue")
print("Updated Table")

display_student_names_grades()
display_class_average()
display_highest_lowest_grades()

print("Choose an student to update its grade: ")
display_student_names_grades()
target_student = input("Name: ").capitalize()
target_grade = float(input("Grade: ")) 

print("Grade Updated!")
class_students[target_student] = target_grade
option = input("Press anything to continue")

display_student_names_grades()
display_class_average()
display_highest_lowest_grades()
