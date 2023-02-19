#0 1 1 2 3 5 8 13 21.....
#f s t
#  f s t
#    f s t
#      f s t
#        f s t
# t=f+S    then

# n= int(input('enter the limit'))
# f=0
# s=1
# print(f)
# print(s)                            WE CANT EXECUTE THIS PRGRM USING WHILE LOOP
# t=f+s
# while(<=n):
#     t=f+s
#     print(t)
#     f=s
#     s=t

n = int(input('enter the limit'))
f = 0
s = 1
print(f)
print(s)
for i in range(2,n):
    t=f+s
    print(t)
    f=s
    s=t



