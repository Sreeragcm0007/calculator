# comparing 2 values and arrange in ascending eg: 8,3,5,10,7 by bubble it will be (3,5,7,8,10)

x = [4,3,9,5,6,7,8,1,2,3]

for i in range(0,len(x)):
    for j in range(0,len(x)-1):
        if x[j]>x[j+1]:
            c=x[j]
            x[j]=x[j+1]
            x[j+1]=c
print(x)

