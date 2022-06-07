import random
num=int(input("How many numbers would you like? "))
zz=[]
for x in range(0,num):
    e=random.randrange(1,10)
    zz.append(e)
print("Your numbers are "+str(zz))