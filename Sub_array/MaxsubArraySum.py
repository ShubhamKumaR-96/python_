# Find the max subarray sum whose length=k
# -3 4 -2 5 3 -2 8 2 -1 4

def maxSum(A,k):
    maxVal=0
    for i in range(len(A)-k+1):
        s=i
        e=i+k-1
        totalSum=sum(A[s:e+1])
        maxVal=max(totalSum,maxVal)
        
    return maxVal

A=list(map(int,input("Enter the element: ").split()))
k=5
print(maxSum(A,k))    
