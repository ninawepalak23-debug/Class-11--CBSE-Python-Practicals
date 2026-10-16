#Input the values of x and n and print the sum of the following series:
#1-x+x^2-x^3+------x^n
x=int(input("Enter a number: "))
n=int(input("Enter the number of steps: "))
sum=0
sign=1
for i in range(0,n+1):
    p=(x**i)*sign
    sum=sum+p
    sign=sign*(-1)
print("The sum of the series is: ",sum)