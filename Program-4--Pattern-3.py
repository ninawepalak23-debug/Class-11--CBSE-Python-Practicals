# Pattern-3
#   A
#   AB
#   ABC
#   ABCD
#   ABCDE
st='ABCDE'
for i in range(0,len(st)):
    for j in range(0,i+1):
        print(st[j],end="")
    print()
