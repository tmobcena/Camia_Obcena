#=================================================================
#Name:            Teny Faye M. Obcena
#Section:         8 - Camia
#Program Name:    Sum and Difference Calculator
#=================================================================

# Ask for User Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = 0
difference = 0

#Calculate Sum
def  calculate_sum():
    global num1, num2, sum
    sum = num1 + num2
    print(f"Sum: {sum}")

#Calculate Difference
def calculate_difference():
    global num1, num2, difference
    difference = num1 - num2
    print(f"Difference: {difference}")

# Call Functions
calculate_sum()
calculate_difference()
