# Write a function that takes a string as input and returns the counts of vowels in the string.
# Vowels= a,e,i,o,u (uppercase aur lowercase )

# input: "hello"

def cntVowels(s):
    vowels="aeiou"

    cnt =0

    for x in s.lower():
        if x in vowels:
            cnt+=1

    return cnt

print(cntVowels("hello"))        
   

            
            
