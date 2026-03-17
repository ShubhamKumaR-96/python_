# Print Col Sum

def printColSum(A):
    rows=len(A)
    col=len(A[0])

    for i in range(col):
        totalSum=0
        for j in range(rows):
            totalSum+=A[j][i]
        print(f"Total sum :{totalSum}")

rows=int(input("Enter rows: "))
cols=int(input("Enter cols: "))

mat=[list(map(int,input(f"Enter row {i+1}: ").split())) for i in range(rows)]

printColSum(mat)