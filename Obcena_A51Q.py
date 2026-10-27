#=================================================================
#Name:            Teny Faye M. Obcena
#Section:         8 - Camia
#Program Name:
#Purpose:         To calculate the average of three activities
#=================================================================

#======================ASK FOR USER INPUT=========================
general_average = float(input("Enter general average: "))
conduct_grade = float(input("Enter conduct grade: "))
failing_grade = (input("Do you have a failing grade? "))

#==================ASSIGN VALUES FOR THE VARIABLES===============
qualified = 0
not_qualified = ""

#======================TEST CONDITIONS===========================
if general_average >= 85:
    qualified += 1
else:
    not_qualified += ("\nNot Qualified: General Average is too low")

if conduct_grade >= 80:
    qualified += 1
else:
    not_qualified += ("\nNot Qualified: Conduct Grade is too low")

if failing_grade == "no":
    qualified += 1
else:
    not_qualified += ("\nNot Qualified: Has a failing grade")

#=====================PRINT OUTPUT============================
if qualified == 3:
    print("Qualified for Scholarship")

else:
    print(f"{not_qualified}")