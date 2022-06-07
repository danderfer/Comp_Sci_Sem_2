num1=int(input("What is your first number? "))
opp=input("What is your oporator? ")
num2=int(input("Second number? "))

if opp=="-":
    print(str(num1)+"-"+str(num2)+"="+str(num1-num2))
elif opp=="+":
    print(str(num1)+"+"+str(num2)+"="+str(num1+num2))
elif opp=="*":
    print(str(num1)+"*"+str(num2)+"="+str(num1*num2))
elif opp=="/":
    print(str(num1)+"/"+str(num2)+"="+str(num1/num2))
else:
    print("Try again, invalid input scum")























#It takes 2 integer inputs
#It takes a String symbol that is an operator
#It can do addition, subtraction, multiplication, and division