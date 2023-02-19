# adding close numbers (0,1,1,2,3,,5,8)


num = int(input("enter"))


n1,n2 = 0, 1 # for storing 2 values

sum = 0

if num < 0:
    print("invalid")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
