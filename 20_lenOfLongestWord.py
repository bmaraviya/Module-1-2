"""Write a Python function that takes a list of words and returns the length of the longest one."""

mystr = "TOPS Technologies is a best IT training and placement institute."

words = mystr.split()
max_len = 0

for i in words:
    if len(i)>max_len:
        max_len=len(i)

print("length of longest word",max_len)
