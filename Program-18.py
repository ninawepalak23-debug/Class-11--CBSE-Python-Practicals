#Search for an element in a list and display its frequency and position.
n=int(input("Enter the number of elements you want in a list: "))
l1=[]
for i in range(n):
    num=int(input("Enter the number: "))
    l1.append(num)
print("The list is: ",l1)
num=int(input("Enter the number you want to check: "))
print("The frequency of",num,"is: ",l1.count(num))
print("The position(s) of",num,"is: ")
for j in range(len(l1)):
    if l1[j] == num:
        print(j + 1, end=" ")

