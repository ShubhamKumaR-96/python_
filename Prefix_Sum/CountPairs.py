# Given String S . find count of pairs such that i<j
# a b c g a g

def countPair(S):
    n=len(S)

    cnt=0

    for i in range(n):
        if S[i]=='a':
            for j in range(i+1,n):
                if S[j]=='g':
                    cnt+=1

    return cnt

def countPairOp(S):
    n=len(S)

    cnt=0
    ans=0
    for i in range(n-1,-1,-1):
        if S[i]=='g':
            cnt+=1
        if S[i]=='a':
            ans+=cnt

    return ans           



S=['a','b','c', 'g','a','g','g']
s=['b','a','c','g','g','a','a','g']
print(f"Total pairs: {countPairOp(s)}")                 
