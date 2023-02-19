# lst=[1,2,3,4,5,6,7]
# def even(n):
#     if(n%2==0):
#         return True  # or n    wrong
#     else:
#         return False
# temp=map(even,lst)
# print(list(temp))


# lst=[1,2,3,4,5,6,7]
# def even(n):
#     if(n%2==0):
#         return n                         right
#
# temp=filter(even,lst)
# print(list(temp))
#
#
# lst=[1,2,3,4,5,6,7]
# def even(n):                                right
#     if(n%2==0):
#         return True
#     else:
#         return False
#
# temp=filter(even,lst)
# print(list(temp))

# lst=[1,2,3,4,5,6,7]
# temp=filter(lambda n:n%2==0,lst)
# print(list(temp))



# lst1=input('enter a elements').split()
# print(lst1)
# temp1=map(int,lst1)
# lst2=list(temp1)
# print(lst2)
#
# temp2=filter(lambda n:n%2==0,lst2)
# temp3=filter(lambda n:n%2!=0,lst2)
# print(list(temp2))
# print(list(temp3))

# lst=['apple','orange','banana','kiwi']
# temp=filter(lambda n:'a' in n,lst)
# print(list(temp))

# lst=['apple','orange','banana','kiwi']
# def member(n):
#     if('a' in n):
#         return n
# temp=filter(member,lst)
# print(list(temp))

# lst=['apple','orange','banana','kiwi']
# list1=[]
# for i in lst:
#     if('a' in i):
#         list1.append(i)
# print(list1)

#using list comphrehension
# lst=['apple','orange','banana','kiwi']
# newlist=[i for i in lst]
# print(newlist)

# lst=['apple','orange','banana','kiwi']
# newlist=[i for i in lst if "a" in i]
# print(newlist)

#list without apple

# lst=['apple','orange','banana','kiwi']
# newlist=[i for i in lst if "apple" not in i]
# print(newlist)

# lst=['apple','orange','banana','kiwi']
# newlist=[i for i in lst if i!='apple']
# print(newlist)

# lst=['apple','orange','banana','kiwi']
# temp=filter(lambda n:'apple' not in n,lst)
# print(list(temp))

# lst=['apple','orange','banana','kiwi']
# def member(n):
#     if('apple' not in n):
#         return n
# temp=filter(member,lst)
# print(list(temp))
#

# lst=['apple','orange','banana','kiwi']
# newlist=[i.upper() for i in lst ]
# print(newlist)

# temp=map(lambda n:n.upper(),lst)
# print(list(temp))

# def member(n):
#     a=n.upper()
#     return a
# temp=map(member,lst)
# print(list(temp))
#
# lst=[2,4]
# newlist=[x+2 for x in lst ]
# print(newlist)
#
#
# lst=[]
# for i in range(0,5):
#     lst.append(i)
# print(lst)

#using list.comp

# lst=[x for x in range(0,5)]
# print(lst)


# lst=['apple','orange','banana','kiwi']
# def change(n):
#     if(n!="banana"):
#         return n
#     else:
#         return "strawberry"
# temp=map(change,lst)
# print(list(temp))


# lst=['apple','orange','banana','kiwi']
# def change(n):
#     if(n=="banana"):
#         return "strawberry"
#     else:
#         return n
# temp=map(change,lst)
# print(list(temp))

#using list.comp
# lst=['apple','orange','banana','kiwi']
# newlst=[i if i!='banana' else "strawberry" for i in lst]
# print(newlst)
#
# lst=['apple','orange','banana','kiwi']
# newlst=["strawberry" if i=='banana' else i for i in lst]
# print(newlst)
#
