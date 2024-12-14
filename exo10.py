word=input("type a word : ")

for i in range(len(word)//2) :
    if word[i]==word[-(i+1)]:
        is_palindrom=True
    else :
        is_palindrom=False
        break

if is_palindrom==True :
    print("Yes, it's a palindrome.")
else :
    print("No, it's not a palindrome.")