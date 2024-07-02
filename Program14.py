# Lcm Of Two Numbers 

num1 = int(input("Enter a value:\n"))

num2 = int(input("Enter a value:\n"))

str = max(num1, num2)
lim = num1*num2

for i in range(str, lim+1, str):
    if i%num1==0 and i%num2==0:
        ans=i
print(ans)