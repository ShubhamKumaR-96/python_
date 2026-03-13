
def queriesVal(A,q):
    n=len(A)

    while q>0:
        startIdx=int(input("Enter Start idx: "))
        endIdx=int(input("Enter end idx: "))
        val=int(input("Enter val: "))

        A[startIdx]+=val
        if endIdx+1 < n:
            A[endIdx+1]-=val

        q-=1

    pf=[0]*n
    pf[0]=A[0]

    for i in range(1,n):
        pf[i]=pf[i-1]+A[i]

    return pf

A=[0,0,0,0,0,0,0]
ans=queriesVal(A,4)
print(ans)    




