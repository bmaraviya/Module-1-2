"""Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string."""

mystr = input("Enter a String:")

index_not = -1
index_poor = -1
start_index = 0

while start_index < len(mystr):
    index_not = mystr.find('not', start_index)
    if index_not == -1:
        break
    index_poor = mystr.find('poor', index_not + 3)
    if index_poor != -1:
        result_string = mystr[:index_not] + 'good' + mystr[index_poor + 4:]
        break
    start_index = index_not + 1

if index_not == -1 or index_poor == -1:
    result_string = mystr

print(result_string)





