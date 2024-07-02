# Linear Search

def linear(array,key):
    
    for i in range(0, len(array)):
        if array[i] == key:
            return i

if __name__ == "__main__":
    
    array=[10,20,30,40,50,60,70,80,90,100]
            
    key = int(input("enter key:"))
    
    answer = linear(array, key)
    
    print(answer)