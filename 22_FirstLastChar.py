"""Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string."""

mystr = input("Enter a string:")  

if len(mystr) < 2:
    result = ""
else:
    result = mystr[:2] + mystr[-2:]

print(result)