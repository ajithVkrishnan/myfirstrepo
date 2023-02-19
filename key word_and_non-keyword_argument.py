# *arg--non keyword argument
# **karg~keyword argument=variable length argument

# def fun(*num):
#     for i in num:
#         print(i,end=" ")
#     print()
# fun(10)
# fun(10,20)
# fun(10,20,30)

#sum of the elements passing

# def sum(*num):
#     s=0
#     for i in num:
#         s=s+i
#     print(s)
# sum(20,30,50)


#**karg~keyword argument=variable length argument

def fun(**karg):
    for key,value in karg.items():
        print(key, 'is' ,value)
fun(name="anu", age=23,cls="bca")


