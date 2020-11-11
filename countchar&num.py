#Write a program that accepts a stringand calculatesthe number of letters and digits.

str = "Edureka123"
charcount=digitcount=0
for item in list(str):       # Iterating through the list of characters
    if(item.isdigit()):
        digitcount+=1
    else:
        charcount+=1

print("LETTERS :- ", charcount, "\nDIGITS :- ",digitcount)

#Output is:
#       LETTERS :-  7 
#       DIGITS :-  3 