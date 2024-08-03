"""Write a Python program to test whether a passed letter is a vowel or not."""

al = input("Enter alphabet:")

vowel = "a,e,i,o,u,A,E,I,O,U"

if al in vowel:
    print(al,"is a Vowel")
else:
    print(al,"is not a Vowel")
