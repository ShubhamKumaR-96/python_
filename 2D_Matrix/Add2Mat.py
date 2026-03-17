# Add 2 matrix

def printAddMat(a,b):
    rows=len(a)
    cols=len(a[0])

    if rows != len(a) or cols != len(b[0]):
        print("Error: matrix dimensions should be same")
        return
    
    res=[]

    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(a[i][j]+b[i][j])
        res.append(row)

    print("After adding two matrix")
    for r in res:
        print(r)    

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter first matrix:")
a = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(rows)]

print("Enter second matrix:")
b = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(rows)]

printAddMat(a, b)

