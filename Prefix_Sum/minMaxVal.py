# Find the max and min in subarray whose length should be minium length subarray
# 2 2 6 4 5 1 5 2 6 4 1

def minMaxLength(A):
    n=len(A)
    minVal=min(A)
    maxVal=max(A)

    ans=float('inf')

    for i in range(n):
        if A[i]==minVal:
            for j in range(i,n):
                if A[j]==maxVal:
                    ans=min(ans,(j-i+1))
                    break

        if A[i]==maxVal:
            for j in range(i,n):
                if A[j]==minVal:
                    ans=min(ans,(j-i+1))
                    break

    return ans

# Optimized way

def minMaxLength2(A):
    n=len(A)
    maxVal=max(A)
    minVal=min(A)
    minIdx= -1
    maxIdx= -1
    ans=float('inf')

    for i in range(n):
        if A[i]==minVal:
            minIdx=i
            if maxIdx != -1:
                ans=min(ans,abs(maxIdx-minIdx)+1)
                
        if A[i]==maxVal:
            maxIdx=i
            if minIdx != -1:
                ans=min(ans,abs(maxIdx-minIdx)+1)
                
    return ans            


A=list(map(int,input("Enter ele: ").split()))
print(f"Min max subarray: {minMaxLength2(A)}")            




