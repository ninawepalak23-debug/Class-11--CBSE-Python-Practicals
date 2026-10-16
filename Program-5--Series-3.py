#Input the values of x and n and print the sum of the following series:
#x+(x^2)/2+(x^3)/3+------+(x^n)/n
x=int(input("Enter a number: "))
n=int(input("Enter the number of steps: "))
sum=0
for i in range(1,n+1):
    p=x**i
    sum=sum+(p/i)
print("The sum of the series is: ",sum)