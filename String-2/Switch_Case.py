# Given a string consisting of only alphabets(either lowercase or uppercase). Print all the characters of string in such a way that for all lowercase character, print its uppercase character and for all uppercase character, print its lowercase character.
# helLO => HELlo

def switchCase(A):

    res=[]
    for char in A:
        if 'A' <= char <='Z':
            res.append(chr(ord(char)+32))
        else:
            res.append(chr(ord(char)-32))
    return "".join(res)

print(switchCase("AdGBhjE"))            
