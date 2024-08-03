"""Write a Python function to insert a string in the middle of a string."""

mystr = input("Enter a string:")

insert_str = input("Enter a string in the middle:")

length = len(mystr)
middle = length//2

new_str = mystr[:middle] + insert_str + mystr[middle:]
print(new_str)