#Write  programs to demonstrate the use of Positional 
#Argument, keyword argument , default arguments , variable 
#length arguments.

#position argument
def add(a,b):
    print("positional argument:",a+b)
    a=(input("Enter number 1:"))
    b=(input("Enter number 2:"))
    add(a,b)

#keyward argument
def show(x,y,name):
    print("keyword argumengt:",(x,y,name))
    show(x=a,y=b,name="suhana")

#default argument
def item(a,b,c=0):
    print("default argument:",a,b,c)
item(a,b,c=10)

#length argument
def var(*args):
    print(args)
    print("length argument:",args)
var(a,b)
    

