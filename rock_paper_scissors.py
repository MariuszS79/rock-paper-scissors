import random
choices=["rock","paper","scissors"]
name=input("Hello, please enter your name: ")
print("Hello "+name+". good luck with your game.")

while True:
    human=input(name+ ",type rock, paper or scissors: ")
    if human not in choices:
      print("are you serious???;-)")
      human=input(name+ ",type rock, paper or scissors: ")
     
    
    computer=(random.choice(choices))
    print("computer chose:"+computer) 
    
    if(human==choices[0] and computer==choices[2]):
        print(name+" won this time, well done "+name)
    elif(human==choices[1] and computer==choices[0]):
        print(name+" won this time, well done "+name)
    elif(human==choices[2] and computer==choices[1]):
        print(name+" won this time, well done "+name)
    elif(human==choices[2] and computer==choices[0]):
        print("Computer won this time, better luck next time")
    elif(human==choices[0] and computer==choices[1]):
        print("Computer won this time, better luck next time")
    elif(human==choices[1] and computer==choices[2]):
        print("Computer won this time, better luck next time")
    else:
        print("Wow, it's a draw ;)")

    print("--------------")
    print("Let's try again ;-)")