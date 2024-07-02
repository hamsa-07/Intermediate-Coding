# Smallest Element in an Array

def smallest(array):
    min = float("inf")
    
    for i in range(len(array)):
        if array[i]<min:
            min = array[i]
    
    return min

if __name__=="__main__":
    array = [7,11,18,-3,-7,4]
    answer = smallest(array)
    print(answer)