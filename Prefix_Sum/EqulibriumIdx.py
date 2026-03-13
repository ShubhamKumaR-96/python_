# Find the equlibrium index
# A= 1 2 3 4 8 10

def equlibriumIdx(A):
    n=len(A)

    for i in range(n):
     leftSum=0
     for j in range(i):
        leftSum+=A[j]
     rightSum=0
     for j in range(i+1,n):
        rightSum+=A[j]

     if leftSum==rightSum:
        return i
     
    return -1  

# Using Prefix way     
def prefixSum(A):
    n=len(A)

    pf=[0]*n
    pf[0]=A[0]

    for i in range(1,n):
        pf[i]=pf[i-1]+A[i]

    return pf    

def equlibrium(A):
   n=len(A)
   pf=prefixSum(A)

   for i in range(1,n):
      leftSum=pf[i-1]
      rightSum=pf[n-1]-pf[i]
      if leftSum==rightSum:
         return i
   return -1   

def optimziedSol(A):
   n=len(A)
   totalSum=sum(A)
   leftSum=0

   for i in range(n):
      rightSum=totalSum-leftSum-A[i]

      if leftSum==rightSum:
         return i
      
      leftSum+=A[i]

   return -1   

A=list(map(int,input("Enter the element: ").split()))
print(optimziedSol(A))


