print("enter the test number to check if it is fibonacci")
n=int(input())
a = 0
b = 1
c=1
x=False
z=n
while z!=0:
    if a ==n or b==n:
        x= True
        break
    c=b
    b=a+b
    a=c


    x= False
    z=z-1
if x==False:
    print("given number is not a fibonacci number")
else:
    print("given number is a fibonacci number")