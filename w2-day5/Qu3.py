###Fizz Buzz - if a number is divisible by 3 - print Fizz, if a number is divisible by 5 - print Fuzz, if a number is divisible by both - print
####Fizz-Buzz.

num = int(input("Enter a number:"))
if(num%3 == 0):
    print("Fizz")
if(num%5 == 0):
    print("Fuzz")
if((num%3 == 0) and (num%5 ==0)):
    print("Fizz-Buzz")

