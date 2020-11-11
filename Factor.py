# Write a program to find the factors of agiven number and check whether the factor is even or odd. 

num = 20
for i in range(1,num+1):
    if(num % i == 0):
        if(i%2 == 0):
            print("Even : ", i)
        else:
            print("Odd : ", i)
    else:
        continue



# Output for 20 is 
# Odd :  1
# Even :  2
# Even :  4
# Odd :  5
# Even :  10
# Even :  20