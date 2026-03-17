# Print 2D Matrix

def printMat(A):
    n=len(A)
    m=len(A[0])
    for i in range(n):
        for j in range(m):
            print(A[i][j],end=" ")
        print()
A=[[1,2,3],[4,5,6],[7,8,9]]
printMat(A)        
