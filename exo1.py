name=str(input("Please enter your name: "))
if name.upper()!="VIP" : 
    nbrticket=int(input("How many tickets would you like to buy?"))
    prixtotal=nbrticket*15.50
    print("The total cost is: ",prixtotal)
    print("Enjoy your tickets!")
elif name.upper()=="VIP":
    print("Enjoy the show for free!")

