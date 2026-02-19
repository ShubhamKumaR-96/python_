# Transformations

price="1234,56"

print(price.replace("," , "."))

price="$123,65.52"
print(price.replace("$", "").replace(",", ""))


phone="+49 (176) 123-4567"
remove_char=" ()-"
cleaned=phone.translate(str.maketrans("","",remove_char))
print(cleaned)

folder='c:/desktop/'
file='report.csv'
print(folder+file)

# print(f" valid : ")

name="shubh-25-INDIA"
print(name.split("-"))

stamp="2026-09-20 14:30"
print(stamp.split(" "))

print("="*30)

# Index and slicing

sl="helloworld"

print(sl[0:10:3])