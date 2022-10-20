####Write a program to find biggest number out of three positive numbers, given by user

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if(a>b):
    if(a>c):
        print("Bigger number is :",a)
elif(b>c):
    print("Bigger number is:",b)
else:
    print("Bigger number is :",c)