inum=int(input("How many items would you like to buy? "))
total=0
for con in range(0,inum):
    item=(input("What are you getting? "))
    cost=float(input("How much is it? "))
    total=total+cost
    print("Thank you for purchesing "+item)
print("Your total is " + str(total)+" for "+str(inum)+" items")