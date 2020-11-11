#Write a program that will find all the numbers between 1000 and 3000 (both excluded) such that each digit of a number is an odd number. Print the number of such elements

for num in range(1001,3000):    
    num1=num
    rem =0 
    flag = True
    while(num!=0):
        rem = num%10
        if(rem %2 ==0):
            flag = False
            break
        else:
            flag = True
        num = num//10

    if(flag == True):
        print(num1)