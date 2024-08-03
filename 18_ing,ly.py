"""Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged."""

mystr = input("Enter a string: ")

if len(mystr) >= 3:
    if mystr.endswith('ing'):
        a = mystr + 'ly'
        print(a)
    else:
        b = mystr + 'ing'
        print(b)
else:
    print(mystr)

