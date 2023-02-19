# #searching an element(key) in a list
#
def linearsearch(list,key):
    n=len(list)
    for i in range(0,n):
        if(list[i]==key):
            return i
    return -1
list1=[11,12,3,65,7]
key1=4
res=linearsearch(list1,key1)
if(res==-1):
    print(key1,'element not found')
else:
    print(key1,'element  found')

