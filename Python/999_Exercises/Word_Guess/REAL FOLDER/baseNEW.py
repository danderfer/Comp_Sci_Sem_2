import random
word_list=[]
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(l)

num= random.randrange(0,12972)
answer= word_list[num]
print(answer)


a=0
for i in range(0,6):
    guess=input("Guess a word ")
    if guess == answer:
        print("YOu won!!!!!!!")
        a=1
        break;
    else:
        print("Sorry, you wong, guess again ")
if a == 0:
    print("You suck and lost, ha the real answer was "+ answer)



f.close()

