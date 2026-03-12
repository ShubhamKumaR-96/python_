# Print all the possible sub array sum
# A=3 -2 4 -1 2 6

def printAllSb(A):
    n=len(A)
    for i in range(n):
        totalSum=0
        for j in range(i,n):
            totalSum+=A[j]
            print(f"Total sum :{totalSum}")

A=list(map(int,input("Enter the element: ").split()))
printAllSb(A)