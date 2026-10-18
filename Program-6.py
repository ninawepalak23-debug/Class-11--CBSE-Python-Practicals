# Determine whether a number is a perfect number, Armstrong Number or Palindrome
n=int(input("Enter a number: "))
sum_p=0
sum_a=0
y=len(str(n))
n1=str(n)
#Perfect Number- a number is perfect if it is equal to the sum of its proper divisors.
for i in range(1,n):
    if n%i==0:
        sum_p=sum_p+i
if sum_p==n:
    print(n,"is a Perfect Number")
else:
    print(n,"is not a Perfect Number")

#Armstrong number is a number that equals the sum of its own digits,
# where each digit is raised to the power of the total number of digits.
for i in range(0,y):
    x=((int(n1[i]))**y)
    sum_a=sum_a+x
if sum_a==int(n):
    print(n,"is an Armstrong Number")
else:
    print(n,"is not an Armstrong Number")

#Palindrome number is any number that stays the same when its digits are reversed
if n1==n1[::-1]:
    print(n,"is a Palindrome Number")
else :
    print(n,"is not a Palindrome Number")