# Sum of numbers in a given range

a = int(input("Enter lower range value:\n"))
b = int(input("Enter Higher range value:\n"))

sum = 0

for i in range(a, b+1):
    sum += i

print(sum)