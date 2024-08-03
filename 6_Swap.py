"""Write python program that swap two number with temp variable and without temp variable."""

a = int(input("Enter number:"))
b = int(input("Enter number:"))

temp = a
a = b
b = temp 
print("swapping:", a)
print("swapping:",b)

#without third variable
print("-------")
print("Without third variable")
a = int(input("Enter number:"))
b = int(input("Enter number:"))

a,b = b,a
print("swapping:", a)
print("swapping:",b)