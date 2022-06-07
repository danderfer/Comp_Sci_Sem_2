sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"

whale_num=0
y=0
for x in range(0,len(sentence)):
    y=y+1
    if sentence[x:y] == "w":
        if sentence[x:y+4] == "whale":
            whale_num=whale_num+1
    elif sentence[x:y] == "W":
        if sentence[x:y+4] == "Whale":
            whale_num=whale_num+1
        

print(whale_num)






with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()

        whale_num=0
        y=0
        for x in range(0,len(sentence)):
            y=y+1
            if sentence[x:y] == "w":
                if sentence[x:y+4] == "whale":
                    whale_num=whale_num+1
                 
            elif sentence[x:y] == "W":
                if sentence[x:y+4] == "Whale":
                    whale_num=whale_num+1
        print(whale_num)
        
    
f.close()