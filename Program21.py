# Frequency of elements in an Array

def frq(array):
    
    n=len(array)
    visit = [False]*n
    
    for i in range(n):
        if not visit[i]:
            count = 1
            for j in range(i+1, n):
                
                if array[i] == array[j]:
                    
                    count+=1
                    visit[j]=True
            print(f"{array[i]} :{count}")

if __name__=="__main__":
    arr = [1, 3, 2, 1, 4, 2, 5, 6, 3, 3, 4]
    frq(arr)