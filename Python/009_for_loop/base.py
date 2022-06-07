dix=input("Do you want a vertical or horizontal line? V for vertical, h for horizontal. ")
dis=int(input("How long? "))     

if dix == "v":
    for cun1 in range(0,dis):
        print("*")
elif dix == "h":
    for cun1 in range(0,dis):
        print("*", end=" ")
else:
    print("You big dumb dumb")