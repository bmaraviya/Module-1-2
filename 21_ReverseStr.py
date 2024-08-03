"""Write a Python function to reverses a string if its length is a multiple of 4."""

str = input("Enter a string:")  

if len(str) % 4 == 0:
    str = str[::-1]  

print(str)
