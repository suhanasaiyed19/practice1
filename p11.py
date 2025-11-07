#write a program to search and element in the list using for loop
#and also demonstrate the use of "else" with for loop.
lst=[10,20,30,40,50]

x=int(input("Enter elemnts to search:"))

for i in lst:
    if i==x:
        print("Element found")
        break
    
else:
    print("Element not found")