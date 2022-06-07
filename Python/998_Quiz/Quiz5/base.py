num= input("What is your favorite number?  Use complete sentancecsece! \n")
old= int(input("Now, how old are you?  Use only the number! \n"))
for x in range(0,len(num)):

    if(num[x:x+1]== 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0):
        
        
        for y in range(0,len(num)):
            if (num[x+y:x+y+1]== " "):
                num=num[x:x+y]
                break 
print(num*old)