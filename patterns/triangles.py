# *
# **
# ***
# ****

# num = int(input("enter :"))
# for i in range(1,num+1): # for rows
#     for j in range (1,i+1): # for column
#         print("*",end=" ")
#     print()


#    *
#   *  *
#  *  *  *

# num = int(input("enter: "))
#
# for i in range(0,num):
#     for j in range(0,num-i-1): # space only
#         print(end=" ")
#
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

#  * * *
#  * *
#   *

num = int(input("enter: "))

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")

    for j in range(0,i):
        print("*",end=" ")
    print()








