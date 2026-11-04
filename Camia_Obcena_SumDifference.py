#=================================================================
#Name:            Teny Faye M. Obcena
#Section:         8 - Camia
#Program Name:    Sum and Difference Calculator
#=================================================================

# Ask for User Input
#Global variables: num1 and num2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Calculate Sum
def  calculate_sum():
    # Local variable: sum
    sum = num1 + num2
    print(f"Sum: {sum}")

#Calculate Difference
def calculate_difference():
    # Local variable: difference
    difference = num1 - num2
    print(f"Difference: {difference}")

# Call Functions
calculate_sum()
calculate_difference()
