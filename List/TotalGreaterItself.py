# Given an array with size N. Count the numbers of elements that have atleast 1 element greater than itself Note => i!j
# 3 -2 6 8 4 8 5

def countGreater(A):
    n=len(A)
    max_val=max(A)
    count=0

    for i in range(n):
        if A[i]>max_val:
            max_val=A[i]

    for num in A:
        if num==max_val:
            count+=1        
    
    return (n-count)

A=list(map(int,input("Enter the ele: ").split()))

print(f"Total greater: {countGreater(A)}")        
