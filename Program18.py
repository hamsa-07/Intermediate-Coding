# Bubble Sort Code

def bubble(array):
    
    for i in range(0, len(array)):
        
        for j in range(len(array)-i-1):
            
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j] 
    
    return array

if __name__ =="__main__":
    array = [64, 34, 25, 12, 22, 11, 90 ]
    
    answer = bubble(array)
    
    for i in range(len(answer)):
        print(array[i])
    