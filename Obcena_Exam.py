# Name:            Teny Faye M. Obcena
# Section:         8 - Camia
# Program Name:    Student Activity Registration System

success = 0
name = input("Enter your name: ").strip()

try:
    age = float(input("Enter your age: "))
    if age >= 12 and age <= 18:
        success += 1
    else:
        print("Invalid Age")

except ValueError:
    print("Invalid age. Enter a whole number.")

activity = ["robotics", "coding", "science", ]
input_activity = input("Choose your activity: ").lower()

if name == "":
    print("Invalid name.")
else:
    success += 1

if input_activity in activity:
    success += 1
else:
    print("Invalid Activity")

if success == 3:
    print("Registration Successful")