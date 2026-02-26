# Without using inbuilt function

s="hello world"



def reverseChar(s):

    res=""

    for i in range(len(s)-1 , -1, -1):
        res+=s[i]

    return res

print(reverseChar(s))    




