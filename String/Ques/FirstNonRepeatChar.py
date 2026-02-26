# Write a function that takes a string as input and return the first character that does not repeat in the string.
# If all characters repeat return None

def firstChar(S):
    count={}

    for char in S:
        count[char]=count.get(char,0)+1

    for char in S:
        if count[char]==1:
            return char

    return None

print(firstChar("hello"))        