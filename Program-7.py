# Input a number and check whether it is prime or composite.
n=int(input('Enter a number: '))
if n==1:
    print('It is neither prime nor composite number')
else:
    for i in range(2,n):
        if n%i==0:
            print("It is a composite number")
            break
    else:
        print("It is a prime number")