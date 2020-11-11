#Design a code which will find whether the given number is Palindrome number or not.


my_number1 = 16261     # Here is the first number to check 
my_number2 = 2314      # Here is the second number to check

rev = rem =0           # Initilizing these variables

num = my_number1  

while(num != 0):
    rem = num % 10
    rev= rev * 10 + rem
    num = num // 10

if (my_number1  == rev):
    print("Congrats! your number is palindrom")
else:
    print("Sorry! your number is not palindrom")
