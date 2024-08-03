"""Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string."""

str1 = "Hello"
str2 = "Bansi"

if len(str1) >= 2 and len(str2) >= 2:
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    x = new_str1 + " " + new_str2

    print(x)
