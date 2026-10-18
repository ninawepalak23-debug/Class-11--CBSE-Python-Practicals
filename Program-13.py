# Input a list of numbers and
# swap elements at even locations with elements at odd locations.
n=int(input("Enter the number of elements you want in a list: "))
l1=[]
for i in range(n):
    num=int(input("Enter the number: "))
    l1.append(num)
print("The list is: ",l1)
for i in range(0,n-1,2):
    l1[i], l1[i+1]=l1[i+1],l1[i]
print("The list is: ",l1)
