# Armstrong Numbers in a given Range

def armstrong_number(num):
    
    expo = len(str(num))
    temp = int(num)
    armstrong = 0

    while temp != 0:
        rem = temp%10
        armstrong += pow(rem, expo)
        temp = temp//10

    if armstrong == num:
        return True
    else:
        return False

if __name__ == "__main__":
    a=int(input("Enter low range:\n"))
    b=int(input("Enter upper range:\n"))
    
    for i in range(a, b+1):
        if armstrong_number(i):
            print(i)