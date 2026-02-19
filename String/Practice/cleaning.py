# whitespace cleanup
text="  Engineering"
print(text.lstrip())

name="  shubh  "
print(name.strip())

txet="Data Engineering#"
print(txet.strip("#"))

text="  Engineer"
print(len(text)==len(text.strip()))
ans=len(text)-len(text.strip())
print(ans)

# Case Conversion

text="Python PROGRAMING"
print(text.lower())

search="Email"
data="email"
print(search.lower()==data.lower())


# Challenges
import re

S = "968-Maria, ( Data Engineer );; 27y  "

# 1. Remove unwanted characters (digits, special chars except letters and spaces)
cleaned = re.sub(r"[^a-zA-Z ]", "", S)

# 2. Split words
words = cleaned.split()

# 3. Extract info
name = words[0]              # Maria
profession = " ".join(words[1:3])  # Data Engineer
age = re.search(r"\d+", S).group() # 27

# 4. Print formatted sentence
print(f"My name is {name} and I am {profession}. My age is {age} now.")


# Search

phone="+48-176-12345"
ans=phone[phone.find("-")+1:]
print(ans)

# Validation

country="INDIA"
print(country.isalpha())