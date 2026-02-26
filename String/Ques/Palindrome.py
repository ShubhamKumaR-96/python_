# Write a function that takes a string as input and returns True if the string is a palindrome
# Otherwise return False
# input = "madam" => output: True

def palindrome(s):

    s=s.lower()

    ans=s[::-1]

    for i in range(len(s)):
        if s[i]!=ans[i]:
            return False
        
        return True

print(palindrome("madma"))     
