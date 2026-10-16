# Input three numbers and display the largest/smallest number.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
    if b>c:
        print(a, "is greatest and",c,"is smallest number")
    else:
        print(a,"is greatest and",b,"is smallest number")
elif b>a and b>c:
    if a>c:
        print(b, "is greatest and",c,"is smallest number")
    else:
        print(b,"is greatest and",a,"is smallest number")
else:
    if a>b:
        print(c,"is greatest and",b,"is smallest number")
    else:
        print(c,"is greatest and",a,"is smallest number")