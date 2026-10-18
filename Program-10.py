#Count and display the number of vowels, consonants,
# uppercase characters, and lowercase characters in a string.
st=input("Enter a word: ")
sum1=0
sum2=0
sum3=0
sum4=0
for i in st:
    #For counting vowels
    if i in 'AEIOUaeiou':
        sum1=sum1+1
    # For counting consonants
    elif i not in 'AEIOUaeiou' and i.isalpha():
        sum2=sum2+1

    #For counting Uppercase Characters
    if i.isupper():
        sum3=sum3+1
    #For counting Lowercase Characters
    elif i.islower():
        sum4=sum4+1
print("Number of vowels in",st,"is: ",sum1)
print("Number of consonants in",st,"is: ",sum2)
print("Number of Uppercase characters in",st,"is: ",sum3)
print("Number of Lowercase characters in",st,"is: ",sum4)