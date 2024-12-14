word=input("veillez entrer votre word : ")
vowel=['a','o','e']
for v in vowel :
    if v in word :
        print(f"{v} found")
    else :
        print(f"{v} not fount")