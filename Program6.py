# Prime Numbers in a given Range
import math
def prime(num):
    
    count = 0
    
    if num < 2:
        print("Not a prime Number")
    else:
        for i in range(3, num + 1):
            if num % i == 0:
                count += 1
    
    if count > 1:
        print(f"{num} is Not Prime Number")
    else:
        print(f"{num} is Prime Number")
    

if __name__ == "__main__":
    a = int(input("Enter low range value:\n"))
    b = int(input("Enter high range value:\n"))

    for i in range(a, b+1):
        prime(i)

'''
import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # other even numbers are not prime
    
    max_divisor = math.isqrt(num) + 1  # only check up to sqrt(num)
    for i in range(3, max_divisor, 2):  # check odd numbers from 3 upwards
        if num % i == 0:
            return False
    
    return True

def primes_in_range(a, b):
    primes = []
    for num in range(max(a, 2), b + 1):  # start from max(a, 2) to handle cases where a < 2
        if is_prime(num):
            primes.append(num)
    
    return primes

if __name__ == "__main__":
    a = int(input("Enter low range value:\n"))
    b = int(input("Enter high range value:\n"))
    
    primes = primes_in_range(a, b)
    for prime in primes:
        print(f"{prime} is Prime Number")

'''