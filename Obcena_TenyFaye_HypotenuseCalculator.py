#==================================================================================
#Program: Hypotenuse Calculator
#Author:  Teny Faye M. Obcena
#Date:    August 26, 2026
#Purpose: This program calculates the hypotenuse of a right-angled triangle.
#===================================================================================

import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"\nThe hypotenuse is: {c:.2f}")