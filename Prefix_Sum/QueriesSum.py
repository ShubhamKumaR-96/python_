A=[-3,6,2,4,5,2,8,-9,3,1]

def queriesSum(A,q):
    
    while q>0:
        startIdx=int(input("Enter startIdx: "))
        endIdx=int(input("Enter endidx: "))
        
        totalSum=0
        for i in range(startIdx,endIdx+1):
            totalSum+=A[i]
        
        print(f"totalSum: {totalSum}")
        
        q-=1


# Using Prefix Sum

def prefixSum(A):
    n=len(A)

    pf=[0]*n
    pf[0]=A[0]

    for i in range(1,n):
        pf[i]=pf[i-1]+A[i]

    return pf

def queriesSums(A,q):
    n=len(A)

    pf=prefixSum(A)

    while q>0:
        s=int(input("Enter Start idx: "))
        e=int(input("Enter the end idx: "))

        if s>0:
            totalSum=pf[e]-pf[s-1]
        else:    
            totalSum=pf[e]
        print(f" Total sum :{totalSum}")

        q-=1       
            
        
queriesSums(A,1)        
            