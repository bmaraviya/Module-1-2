"""Write a Python program to check if a number is positive, negative or zero."""

num = int(input("Enter your number:"))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
elif num == 0:
    print("Zero")