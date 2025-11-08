#Write a program to create a list using range functions and
#perform append, update and delete elements operations
#in it.
lst=list(range(1,11))
print("original list=",lst)

lst.append(50)
print("after append list=",lst)

lst[2]=100
print("after update list=",lst)

del lst[5]
print("delete list=",lst)