#substring


str = input("enter a value: ")

substring = input("enter substring: ")

print(str.find(substring))

if str.find(substring)==-1:
    print("not found")
else:
    print("found")