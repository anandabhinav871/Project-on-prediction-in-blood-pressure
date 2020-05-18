#Write a program to find a given number is Armstrong number or not.

n=int(input("Enter a number:- "))
sum=0
temp=n
length= len(str(n))
while(temp>0):
    dig=temp%10
    sum=sum+(dig**length)
    temp=temp//10

if(sum==n):
    print("Armstrong number")
else:
    print("Not a armstrong number")
    
