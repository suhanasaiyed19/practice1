#Write a program to generate prime numbers with the help of a function to test prime or not. 

def prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=int(input("Enter number:"))

print("prime numbers from 1 to",num,"are:")
for i in range(1,num+1):
    if prime(i):
        print(i)


if  prime(num):
     print(num,"is prime number")
 
else:
    print(num,"is not a prime number")



    