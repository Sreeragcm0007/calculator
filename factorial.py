# 5 = 5*4*3*2*1 factorial

i = int(input("enter a value: "))

fac = 1  # number to multiply by 1

while i > 0:
    fac = fac *i
    i = i -1

print("factor = ",fac)
