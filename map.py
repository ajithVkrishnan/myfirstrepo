#1 lst=['1','2','3']  strint list
# temp=map(int,lst)
# print(list(temp))

#2 lst=[1,2,3,4] :make list of squares

# def square(n):      fn nmae:square
#     return n*n
# lst=[1,2,3,4]
# temp=map(square,lst)
# print(list(temp))

#3using lamda function
#
# square= lambda n:n*n    #fun nmae:squre
#
#
# lst=[1,2,3,4]
# temp=map(square,lst)
# print(list(temp))

       #OR
# lst=[1,2,3,4]
# temp=map(lambda n:n*n,lst)
# print(list(temp))
#     can use tuple also


#4 adding elements of 2 lists and the sums are amde into another list
# list1=[1,2,3,4,5]
# list2=[1,2,3,4,6]
# sumoflist= lambda a,b:a+b
# temp=map(sumoflist,list1,list2)
# print(list(temp))

   #OR

# list1=[1,2,3,4,5]
# list2=[1,2,3,4,6]
# temp=map(lambda a,b:a+b,list1,list2)
# print(list(temp))

# n=input('enter elemnts').split()
# print(list(n))

# a="sat"
# print(list(a))


#5 lst=['sat','bat','hat']
# def sample(n):
#     return list(n)
# temp=map(sample,lst)
# print(list(temp))

# a=1
# print(list(a))
#OR
# lst=['sat','bat','hat']
# temp=map(list,lst)
# print(list(temp))
#OR

# lst=['sat','bat','hat']
# temp=map(lambda n:list(n),lst)
# print(list(temp))
