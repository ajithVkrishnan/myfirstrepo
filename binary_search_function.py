# def binarysearch(list,key):
#     start=0
#     end=len(list)-1
#     mid=0
#     while(start<=end):
#         mid=(start+end)//2
#         if(key>list[mid]):
#             start=mid+1
#         elif(key<list[mid]):
#             end=mid-1
#         else:
#             return mid
#     return -1
#
# list1=[1,8,2,3,9,4,5]
# list1.sort()
# print(list1)
# key1=3
# res=binarysearch(list1,key1)
# if(res==-1):
#     print(key1,"is not found")
# else:
#     print(key1,'is found at index postiton',res)




# def binarysearch(list,key):
#     start=0
#     end=len(list)-1
#
#     while(start<=end):
#         mid=(start+end)//2
#         if(key>list[mid]):
#             start=mid+1
#         elif(key<list[mid]):
#             end=mid-1
#         else:
#             return mid,mid
#     return -1
#
# list1=[1,2,3,3,4,5,6]
# list1.sort()
# print(list1)
# key1=3
# ot,res=binarysearch(list1,key1)
# print(res)
# print(ot)
# if(res==-1 and ot==-1):
#     print(key1,"is not found")
# else:
#     print(key1,'is found at index postiton',res,'and',ot)

# value=12
# def sample():
#     c=value+2
#     print(c)
# sample()

n=input('enter a no').split()
list=list(n)
print(list)
print(n)


