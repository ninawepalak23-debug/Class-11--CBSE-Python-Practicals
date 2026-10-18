#Input a string and determine whether it is a palindrome;
# convert the case of characters in the string.
st=input("Enter a word: ")
if st.lower()==st.lower()[::-1]:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")