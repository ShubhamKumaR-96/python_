# Write a function that takes a string as input and return a new string with all duplicate characters removed, 
# keeping only the first occurence of each character
# Input: "Hello"

def remove_dup(S):

    seen=set()
    result=""

    for char in S:
        if char not in seen:
            seen.add(char)
            result+=char

    return result

print(remove_dup("hello"))        





