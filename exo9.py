nompays=input("entrer le nom de votre cité: ")
listnom=[]
listlong=[]

while nompays!="stop" :
    listnom.append(nompays)
    long=len(nompays)*1000000
    listlong.append(long)
    nompays=input("entrer le nom de votre cité: ")

for i in range(len(listnom)):
    print(f"The city {listnom[i]} has {len(listnom[i])} letters, so its population is {listlong[i]}")
