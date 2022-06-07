sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"


count = 0
with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        #print(sentence)
        ##YOUR CODE GOES HERE
        for i in range(len(sentence)-4):
            #print(sentence[i:i+5].lower())
            if(sentence[i:i+5].lower() == "whale"):
                count+=1

print(count)
f.close()
