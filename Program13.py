# HCF/GCD of two numbers

num_1 = int(input("Enter a number:\n"))
num_2 = int(input("Enter a number:\n"))

lim = min(num_1, num_2)

for i in range(1, lim+1):
    if num_1%i==0 and num_2%i==0:
        print(i) 

'''
while num2 != 0:
    num1, num2 = num2, num1 % num2
return num1
'''