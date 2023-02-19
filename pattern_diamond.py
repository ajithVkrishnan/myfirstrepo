# Diamond pattern

# row= int(input('Enter number of row: '))
#
# upper part
# for i in range(1, row+1):
#     for j in range(1,row-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()

# Lower part of diamond
# for i in range(row,0, -1):
#     for j in range(1,row-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()
# #
# n = int(input('Enter number of row: '))
#
# for i in range(1,n+1):
#     for k in range(1,i):
#         print(" ",end="")
#     for j in range(1,(n+6)-2*i):
#         print("*", end="")
#     print()