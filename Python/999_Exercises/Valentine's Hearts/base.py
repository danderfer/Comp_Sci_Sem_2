


#It is convoluted and I don't care

import random

people=[]
complement=[]
with open('People.txt') as f:
    for line in f:
        l = line.strip()
        people.append(l)

with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        complement.append(l)

for qqqqq in range(0,20):   #This is so I can see more at a time

    x=random.randrange(1,len(people))

    W1=people[x]

    x=random.randrange(1,len(complement))

    W2=complement[x]

    print(W1+" is "+W2 )


f.close()
