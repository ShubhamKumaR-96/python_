# Rotate Matrix clock wise

def rotateMat(A):
    n=len(A)

    # first transpose the mat
    for i in range(n):
        for j in range(n):
            A[i][j],A[j][i]=A[j][i],A[i][j]

    # reverse the mat

    for i in range(n):
        A[i].reverse()

    return A
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
ans=rotateMat(A)
print(f"After rotating Mat : {ans}")            