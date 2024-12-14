print("Runner 1:")
name1=input("Name: ")
time1=int(input("Time (in seconds):"))

print("Runner 2:")
name2=input("Name: ")
time2=int(input("Time (in seconds):"))

if time1<time2 :
    print("The faster runner is ",name1)
elif time1>time2 :
    print("The faster runner is "+name2)
elif time1==time2 :
    print(f"{name1} and {name2} have the same time")