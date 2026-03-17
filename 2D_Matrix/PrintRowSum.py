# Print Row wise Sum

def printRowSum(A):
    rows=len(A)
    col=len(A[0])

    for i in range(rows):
        totalSum=0
        for j in range(cols):
            totalSum+=(A[i][j])
        print(f"Row Sum : {totalSum}")



rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
mat=[]
for i in range(rows):
    row=list(map(int,input(f"Enter row {i+1} element:").split()))
    mat.append(row)

printRowSum(mat)  
         
