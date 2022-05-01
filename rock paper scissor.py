from random import randint

#create a list of play options
t = ["rock", "paper", "scissor"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

b=0
c=0
a=int(input("Game for how many points?    "))

for i in range(a):
#set player to True
    player = input("rock, paper, scissor?       ")
    if player == computer:
        print("Tie!")
        print("your point:",b)
        print("computer point:",c)
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
            b=b-1
            c=c+1
            print("your point:",b)
            print("computer point:",c)
        else:
            print("You win!", player, "smashes", computer)
            b=b+1
            c=c-1
            print("your point:",b)
            print("computer point:",c)
    elif player == "paper":
        if computer == "scissor":
            print("You lose!", computer, "cut", player)
            b=b-1
            c=c+1
            print("your point:",b)
            print("computer point:",c)
        else:
            print("You win!", player, "covers", computer)
            b=b+1
            c=c-1
            print("your point:",b)
            print("computer point:",c)
    elif player == "scissor":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
            b=b-1
            c=c+1
            print("your point:",b)
            print("computer point:",c)
        else:
            print("You win!", player, "cut", computer)
            b=b+1
            c=c-1
            print("your point:",b)
            print("computer point:",c)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    computer = t[randint(0,2)]
if b>c:
    print('You win',b,'is your point')
elif b==c:
    print('Game is tie')
else:
    print('You loose',b,'is your point')
