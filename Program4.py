# Check if Leap Year or not

year = int(input("Enter Year:\n"))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("Leap Year!")
else:
    print("Not a leap Year")