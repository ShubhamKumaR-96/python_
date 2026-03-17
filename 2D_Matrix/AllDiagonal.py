# Print All the diagonal

def printDiagonal(A):
    n=len(A)
    m=len(A[0])

    for col in range(m):
        i=0
        j=col
        while i<n and j<m:
            print(A[i][j],end=" ")

            i+=1
            j+=1
        print()

    for row in range(1,n):
        i=row
        j=0
        while i<n and j<m:
            print(A[i][j], end=" ")
            i+=1
            j-=1
        print()

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
printDiagonal(A)                  

