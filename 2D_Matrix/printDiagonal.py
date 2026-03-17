# Print Diagonal left to right

def printDiagonal(a):
    row=len(a)
    col=len(a[0])

    for i in range(row):
        print(f"Diagonal left to right {i+1} : {a[i][i]}")

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))    

mat=[list(map(int,input("Enter ele: ").split())) for i in range(rows)]
printDiagonal(mat)

