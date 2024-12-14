x=int(input("combien de perssones ont besoins defaire un trajet :"))
y=int(input("combien de perssones un taxi peut transporter:"))
#z=x//y
t=x%y
if t==0 :
    print("le nombre de taxi est "+str(x//y))
elif t!=0 :
    print("le nombre de taxi est "+str(x//y+1))
print("merci")
