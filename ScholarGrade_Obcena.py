

#Display title and ask for user inputs
print("===== PSHS SCHOLAR GRADE CALCULATOR =====")
name = input("Enter student name: ")
quiz1 = int(input("Enter Quiz 1 score: "))
quiz2 = int(input("Enter Quiz 2 score: "))
quiz3 = int(input("Enter Quiz 3 score: "))
perfect_score = 60

#Add the quizzes for the total
def calculate_total(quiz1, quiz2, quiz3):
    return quiz1 + quiz2 + quiz3

#Divide total by three for average
def calculate_average(total):
    return total / 3

#Divide the perfect score by the total for the percentage
def calculate_percentage(total, perfect_score):
    return total / perfect_score * 100

#Call functions
total = calculate_total(quiz1, quiz2, quiz3)
average = calculate_average(total)
percentage = calculate_percentage(total, perfect_score)

#Display student report
print("========== STUDENT REPORT ==========")
print(f"Student Name: {name}")
print(f"Total Score: {total} out of 60")
print(f"Average Score: {average:.2f}")
print(f"Percentage Score: {percentage:.2f}%")
