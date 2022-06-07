mynumbers = [6,9,32,28,15,22,3,18]
average=0
add=0
for x in range(0,len(mynumbers)):
    add=add+mynumbers[x]
average=add/(len(mynumbers))

y=0
fixnum=mynumbers
minn = 0

for x in range(0,len(mynumbers)):
    y=y+1
    if len(mynumbers)==0:
        break
    if fixnum[x] > fixnum[y]:
        fixnum.remove(x)
    else:
        fixnum.remove(y)

minn = fixnum[0]


y=0
fixnum=mynumbers
maxx = 0

for x in range(0,len(mynumbers)):
    y=y+1
    if len(mynumbers)==0:
        break
    if fixnum[x] < fixnum[y]:
        fixnum.remove(x)
    else:
        fixnum.remove(y)

maxx = fixnum[0]