# Write a code that accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically

str1 = "Banana Apple Orange Guava"
lst1 = str1.split(" ")     #It will create list of words 
print(lst1)                #It will print the list before sorting
lst1.sort()                #It will sort the list
print(lst1)                #It will print the list after sorting

#Output: 
#        ['Banana', 'Apple', 'Orange', 'Guava']
#        ['Apple', 'Banana', 'Guava', 'Orange']