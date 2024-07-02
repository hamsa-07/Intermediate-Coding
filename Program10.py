# Armstrong Number Implimentation
num = input("Enter a number:\n")

expo = len(num)
temp = int(num)
armstrong = 0

while temp != 0:
    rem = temp%10
    armstrong += pow(rem, expo)
    temp = temp//10
    
arm = str(armstrong)

if arm == num:
    print("Number is armstrong")
else:
    print("Not a armstrong")
    