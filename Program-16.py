#Find the largest and smallest numbers in a list/tuple
# and display their positions.
n=int(input("Enter the number of elements you want in a list: "))
l1=[]
for i in range(n):
    num=int(input("Enter the number: "))
    l1.append(num)
print("The list is: ",l1)
print("The largest number of the list is: ",max(l1))
print("The position of largest number is:",l1.index(max(l1))+1)
print("The smallest number of the list is: ",min(l1))
print("The position of smallest number is:",l1.index(min(l1))+1)