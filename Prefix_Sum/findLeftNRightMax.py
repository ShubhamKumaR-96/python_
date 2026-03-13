# Find the left max of all element of it's right side and right max element of it's right
# A= -3 6 2 4 7 2 8 -9 3 1

def leftRightMx(A):
    n=len(A)

    leftmax=[0]*n
    rightMax=[0]*n

    leftmax[0]=A[0]
    rightMax[n-1]=A[n-1]

    for i in range(1,n):
        leftmax[i]=max(leftmax[i-1],A[i])

    for i in range(n-2,-1,-1):
        rightMax[i]=max(rightMax[i+1],A[i])

    return leftmax,rightMax

A=list(map(int,input("Enter the element: ").split()))
l,r=leftRightMx(A)
print(f"Left Max: {l}" )
print(f"right Max:{r}")         

    