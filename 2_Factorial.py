"""Write a Python program to get the Factorial number of given number."""

num = int(input("Enter number:"))
a = 1

for i in range(1,num+1):
    a = a * i
print(a)

