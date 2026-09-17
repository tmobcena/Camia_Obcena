#=================================================================
#Name:            Teny Faye M. Obcena
#Section:         8 - Camia
#Date:            September 17, 2026
#=================================================================

#==================== 1. PAYMENT METHOD CHECKER ==================
valid_payment = {"Cash", "GCash", "Card"}
payment_method = input("Enter payment method: ")

if payment_method in valid_payment:
    print("Valid payment method.")

else:
    print("Invalid payment method.")

#======================== 2. GRADE CHECKER =====================
grade = float(input("\nEnter your grade: "))

if 0 < grade <= 100:
    print("Valid grade.")

else:
    print("Invalid grade.")

#======================== 3. STUDENT ID CHECKER =====================
import re
student_ID = input("\nEnter student ID: ")
pattern = r"\d{4}-\d{4}"
if re.fullmatch(pattern, student_ID):
    print("Valid student ID.")

else:
    print("Invalid student ID.")

#======================== 4. PIN VALIDATOR =========================
pin = input("\nCreate a 6-digit PIN: ")
if len(pin) == 6 and pin.isdigit():
    print("Valid PIN.")

else:
    print("Invalid PIN.")

#======================== 5. STUDENT SCORE ENTRY =====================
try:
    score = int(input("\nEnter examination score: "))
    if 0 < score <= 100:
        print("Valid score.")

    else:
        print("Invalid score.")

except ValueError:
    print("Invalid input. Please enter a number.")

