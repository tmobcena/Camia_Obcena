
# Header
def display_header():
    print("=================================================================")
    print("------------------STUDENT PERFORMANCE EVALUATOR------------------")
    print("=================================================================")

# Get student name and assessments
def get_student_info():
    #Local variables: student_info, a_1, a_2, a_3
    student_info = input("Enter student name: ")
    a_1 = float(input("Enter assessment 1: "))
    a_2 = float(input("Enter assessment 2: "))
    a_3 = float(input("Enter assessment 3: "))
    return student_info, a_1, a_2, a_3

#Get average and performance level
def evaluate_performance(a_1, a_2, a_3):
    average = (a_1 + a_2 + a_3)/3
    performance_level = ""

    if 90 <= average <= 100:
        performance_level += "Outstanding"
    elif 85 <= average <= 89:
        performance_level += "Very Satisfactory"
    elif 80 <= average <= 84:
        performance_level += "Satisfactory"
    elif 75 <= average <= 79:
        performance_level += "Fairly Satisfactory"
    else:
        performance_level += "Needs Improvement"

    return average, performance_level

# display inputs
def display_report(student_info, a_1, a_2, a_3,average, performance_level):
    print("STUDENT PERFORMANCE REPORT")
    print(f"Student Name: {student_info}")
    print(f"Assessment Scores: {a_1}, {a_2}, {a_3}")
    print(f"Average Score: {average:.2f}")
    print(f"Performance Level: {performance_level}")

display_header()
#global variable:
student_info, a_1, a_2, a_3 = get_student_info()
average, performance_level = evaluate_performance(a_1, a_2, a_3)
display_report(student_info, a_1, a_2, a_3, average, performance_level)