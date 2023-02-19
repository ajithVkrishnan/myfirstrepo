# import functools
# lst=[1,2,3,4]
# result=functools.reduce(lambda x,y:x+y,lst)
# print(result)
#
# lst=[1,2,3,4]
# result=functools.reduce(lambda x,y:x*y,lst)
# print(result)

# from functools import *
# lst=[1,2,3,4]
# result=reduce(lambda x,y:x+y,lst)
# print(result)


from functools import *
lst=[1,2,3,4]

import operator

result=reduce(operator.add,lst)
product=reduce(operator.mul,lst)
diff=reduce(operator.sub,lst)
print(result)
print(product)
print(diff)

#
# import operator
# cont=dir(operator)
# print(cont)

#largest numbewr in a list
# lst=[1,5,3,4]
# lst.sort()
# n=len(lst)
# print(lst[n-1])


# lst=[1,5,3,4,5]
# from functools import *
# res=reduce(lambda x,y:x if x>=y else y ,lst)
# print(res)
#
# print(max(lst))
#
# lst=[1,5,3,4,5]
# from functools import *
# res=reduce(lambda x,y: max(x,y),lst)
# print(res)

# lst=[1,5,3,4,5]
# from functools import *
# res=reduce(max,lst)
# print(res)



# import functools
# lst=[1,12,3,56]
# def largest(x,y):
#     if(x>=y):
#         return x
#     else:
#         return y
# res=functools.reduce(largest,lst)
# print(res)
