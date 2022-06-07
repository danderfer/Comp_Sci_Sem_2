import random

japs=["shusi", "noodle", "eye"]
beans= ["kindny","lava","black"]
legs=["chicen","human","monkye"]
rests=["japs","beans","legs"]
randnum=random.randrange(0,2)
what= input("We have three resterants "+rests+" where do you want food?")

if what == japs:
    print("we recomend our "+japs[randnum])
elif what == beans:
    print("we recomend our "+beans[randnum])
elif what == legs:
    print("we recomend our "+legs[randnum])
else:
    print("Not an optioin")