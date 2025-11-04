#A simple program that will get the average of the students, who has the higher/lower score, and the user can also update it

def average_calc(numbers : list[float]) -> float:        
    return sum(numbers) / len(numbers)
    
def add_new_student(student_name : str, student_grade : int) -> None:
    class_students[student_name] = student_grade
    
def print_student_names_grades() -> None:
    for student in class_students.keys():   
        print(f"{student} => {class_students[student]}")

class_students : dict = {"Alice" : 85.0, "Bob" : 92.0, "Wallace" : 75.0}

print("\nWelcome to the class room!")
print("Here are our students and their grades: ")

print_student_names_grades()

