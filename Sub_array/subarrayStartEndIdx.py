# Print the starting index and ending index of all subarray whose length=K
# 3 4 2 -1 6 7 8 9 3 2 -1 4 K=6

def printIdx(A,k):
    n=len(A)

    for i in range(n-k+1):
        s=i
        e=i+k-1
        print(f"{s} to {e}: ({s},{e})")

A=list(map(int,input("Enter the element: ").split()))
k=6
printIdx(A,k)        


