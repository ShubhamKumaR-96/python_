# Write a function that takes two strings as input and return True. if they are anagrams of each other otherwise False

def anagram(s,t):
    if len(s)!=len(t):
        return False
    
    count={}

    for char in s:
        count[char]=count.get(char,0)+1

    for char in t:
        if char not in count or count[char]==0:
            return False
        count[char]-=1   


    return True

# print(anagram("listen","silent"))   
print(anagram("aab","abb")) 
            