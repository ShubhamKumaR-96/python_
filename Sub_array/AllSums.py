# Find Sum of all subArray sum
# A=3 -2 4 -1 2 6

def allSums(A):
    n=len(A)
    Sums=0
    for i in range(n):
        totalSum=0
        for j in range(i,n):
            totalSum+=A[j]
        Sums=Sums+totalSum  
    print(f"Total Sums: {Sums}")      

A=list(map(int,input("Enter the element: ").split()))
allSums(A)