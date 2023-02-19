#file open & read

# fo=open('new','r')

# print(fo.read(2))
# print((fo.read(3)))

# print(fo.readline())

# print(fo.readline(2))

# print(fo.readlines())


# a=fo.readlines()

# for i in a:
#     print(i)
#
# for line in a:
#     print(line.strip())
# fo.close()    #should close the file


# print((fo.name))
# print((fo.mode))
# print((fo.closed))


#find the lines ina file

f1=open('new',"r")

a=f1.readlines()   # can also use len(a)  beacuse a is a list
print(a)
fact=0
for i in a:
    fact=fact+1
f1.close()
print(fact)





