# Name:            Teny Faye M. Obcena
# Section:         8 - Camia
# Program Name:    Circular Garden
# Purpose:         To calculate the area and circumference of the garden, find the square root of the area,
#                  and determine the area rounded down and rounded up

#Import math to make the math libraries available
import math

#Ask user input for radius
radius = float(input("Enter radius in meters: "))

#Perform the calculations
area = math.pi * pow(radius, 2)
circumference = 2 * math.pi * radius
squareRoot = math.sqrt(area)
roundDown = math.floor(area)
roundUp = math.ceil(area)

#Display the results
print(f"Area of the garden: {area:.2f} square meters")
print(f"\nCircumference of the garden: {circumference:.2f} meters")
print(f"\nSquare root of the area: {squareRoot:.2f}")
print(f"\nArea rounded down: {roundDown:.2f} square meters")
print(f"\nArea rounded up: {roundUp:.2f} square meters")