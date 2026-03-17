# Print Diagonal right to left

def printDiagonal(a):
    rows=len(a)
    cols=len(a[0])

    if rows != cols:
        print("Rows and cols should be name")
        return

    for i in range(rows):
        print(f"Right to left : {a[i][cols-1-i]}")

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))    

mat=[list(map(int,input("Enter ele: ").split())) for i in range(rows)]
printDiagonal(mat)

