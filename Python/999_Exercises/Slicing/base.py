name=input("What is your first and last name? ")

y= 0
for x in range(0,len(name)):
    y=y+1
    print(name[x:y])

y=0
for x in range(0,len(name)):
    y=y+1
    if name[x:y] == " ":
        print(name[x:len(name)])
        print(name[0:x])