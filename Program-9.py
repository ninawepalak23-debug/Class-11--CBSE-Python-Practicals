n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
ori_n1=n1
ori_n2=n2
while n2>0:
    remainder=n1%n2
    n1=n2
    n2=remainder
print("Greatest Common Divisor of",ori_n1,"and",ori_n2,"is",n1)
LCM=(ori_n1*ori_n2)//n1
print("Least Common Multiple of",ori_n1,"and",ori_n2,"is",LCM)
