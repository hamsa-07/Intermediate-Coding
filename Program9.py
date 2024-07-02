# Program to check if a number is palindrome or not
num = int(input("Enter a number:\n"))

temp = num
rev=0

while temp != 0:
    rem = temp%10
    rev = rev*10+rem
    temp = temp//10

if rev == num:
    print("Number is palindrome")
else:
    print("Not a palindrome")