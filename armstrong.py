# armstrong = sum of number digit = sum of nth power of its digits eg = 5 number of digit = 1 n=1 = 5raise to1 = 5 = yes

i = int(input("enter any number: "))

org = i                                 # for storing i value (because it lost sometime)

sum = 0


while(i>0):
    sum =sum+(i%10)* (i%10)* (i%10)* (i%10) # for cube
    i = i//10                               # for dropping the reminder

if org == sum:
    print("arm")
else:
    print("not")
