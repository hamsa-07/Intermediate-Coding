# print Prime Factors of a Number
import math
num = int(input("Enter a value:\n"))

max = num **2

while num % 2 == 0:
    print(2, end=" ")
    num = num//2
    
for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            print(i, end=" ")
            num = num//i
    
if num > 2:
    print(num)
    