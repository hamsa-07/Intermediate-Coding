# Second Smallest Element in the Array 

def second_smallest(array):
    
    first = float("inf")
    second = float("inf")
    
    for i in range(len(array)):
        if array[i] < first:
            second = first
            first = array[i]
        elif array[i] < second and array[i]!=first:
            second=array[i]
        
    return second
    
if __name__=="__main__":
    array=[7,11,18,-3,-7,4]
    answer = second_smallest(array)
    print(answer)