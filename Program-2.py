#Input two numbers and display the larger/smaller number.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    print(a,"is greater and",b,"is smaller.")
elif a<b:
    print(b,"is greater and",a,"is smaller.")
else:
    print(a,"and",b,"are equal.")