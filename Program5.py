# Prime numbers or not Part 1
num = int(input("Enter a number:\n"))

count = 0

for i in range(1, num):
    if num % i == 0:
        count += 1

if count > 2:
    print("Not a prime number!")
else:
    print("It is prime number")
