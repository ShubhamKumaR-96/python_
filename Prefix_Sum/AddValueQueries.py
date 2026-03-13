# Array Size N. All the elements are equal to zero and we have q queries add value to all elements from index to n-1

def addQuesVal(A,q):
    n=len(A)

    while q>0:
        index=int(input("Enter the index: "))
        val=int(input("Enter Value: "))

        for i in range(index,n):
            A[i]+=val

        q-=1

    return A

def prefixSum(A):
    n=len(A)

    pf=[0]*n
    pf[0]=A[0]

    for i in range(1,n):
        pf[i]=pf[i-1]+A[i]

    return pf

def addQuesVal2(A,q):
    n=len(A)

    while q>0:
        index=int(input("Enter the index: "))
        val=int(input("Enter Value: "))

        A[index]+=val

        q-=1    

    pf=prefixSum(A)

    return pf         

A=[0,0,0,0,0,0,0]
ans=addQuesVal2(A,3)

print(ans)

    