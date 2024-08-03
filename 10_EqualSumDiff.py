"""Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5."""

n1 = int(input("Enter number:"))
n2 = int(input("Enter number:"))
sum = n1+n2
diff = n1-n2

if n1==n2 or sum==5 or diff==5:
    print("true")
else:
    print("false")