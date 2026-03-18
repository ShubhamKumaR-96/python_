def rotateMat(A):
    n = len(A)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i+1, n):   # avoid double swap
            A[i][j], A[j][i] = A[j][i], A[i][j]

    # Step 2: Reverse each column
    for j in range(n):
        for i in range(n//2):
            A[i][j], A[n-1-i][j] = A[n-1-i][j], A[i][j]

    return A


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ans = rotateMat(A)
print("After rotating Anticlockwise:")
for row in ans:
    print(row)