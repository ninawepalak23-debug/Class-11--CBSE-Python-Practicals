#Input a list of numbers,
# check whether a number equals the sum of the cubes of its digits,
# find the largest and smallest numbers in the list.

#Make user defined list
n=int(input("Enter the number of elements you want in a list: "))
l1=[]
for i in range(n):
    num=int(input("Enter the number: "))
    l1.append(num)
print("The list is: ",l1)
#check whether a number equals to the sum of the cubes of its digits,
for i in l1:
    sum1 = 0
    for digit in str(i):
        sum1= sum1+int((digit))**3
    if sum1==i:
        print(i,"equals to the sum of the cubes of its digits")
#To find the smallest and largest number in the list
print("The largest number of the list is: ",max(l1))
print("The smallest number of the list is: ",min(l1))