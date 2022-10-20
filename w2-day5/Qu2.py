###Write a program to find second biggest number out of three positive numbers

from os import lseek


a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

if((a>b) & (b>c)):
    print("second biggest number is:",b)
    