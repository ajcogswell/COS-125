# File: ajCogswell_lab2.py
# Author: Aj Cogswell
# Date: Sept 10
# Section: 0002
# E-mail: anthony.cogswell@maine.edu
# Description:
# Calculates perimeter and diagonal of a rectangle using length and width
# measurements input by the user. Also does some other stuff.

print("Welcome to the Rectangle area calculator")
print(type("Welcome")) #str
print(type(42)) #int
print(type("42")) #str

fav_food = "I'm not thinking about food while hungry, sorry."

print(f"My favorite food is {fav_food}")

age = int(input("What is your age: "))
print(f"I am {age} years old")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

num3 = num1 + num2

print(num1, "+", num2, "=", num3)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rectPerimeter = (length + width) * 2
rectDiagonal = (length ** 2 + width ** 2) ** 0.5

print(length, width, rectPerimeter, rectDiagonal)

print(1/4)
print(1//4)
print(int(1/4))
print(float(1/4))
print(1//4.0)
print(4/2.5)
print(-1//2)
print(2**2)
print(2*2)
print((2*2)**2)
print(8%3)
print(8%2)
print((2**8)+8/12)
print(100+10*(6-2))
print(100+10*6-2)
