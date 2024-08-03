"""Write a Python program to count the occurrences of each word in a given sentence"""

str = input("Enter a string: ")

words = str.split()
index = 0

while index < len(words):
    word = words[index]
    count = 0
    for i in words:
        if word == i:
            count += 1
    if words.index(word) == index:
        print(f"{word}: {count}")
    index += 1


