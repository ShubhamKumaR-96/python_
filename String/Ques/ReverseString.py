# Without using inbuilt function

s="hello world"

def reverseChar(s):

    res=[]

    for i in range(len(s)-1 , -1, -1):
        res.append(s[i])

    return "".join(res)

print(reverseChar(s))    


