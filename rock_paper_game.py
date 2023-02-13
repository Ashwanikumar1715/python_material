import random
while True:
    choices=["rock","paper","scissor"]
    computer=random.choice(choices)
    player=None

    while player not in choices:
        player=input("chose paper scissor or rock\n").lower()

    if player==computer:
        print("computer:",computer)
        print("player:",player)
        print("match tie!!")

    elif player =="rock":
        if computer=="paper":
            print("computer:",computer)
            print("player:",player)
            print("you lose:(")
        if computer=="scissor":
            print("computer:",computer)
            print("player:",player)
            print("you win!!")

    elif player =="paper":
        if computer=="rock":
            print("computer:",computer)
            print("player:",player)
            print("you win!!")
        if computer=="scissor":
            print("computer:",computer)
            print("player:",player)
            print("you lose:(")

    elif player =="scissor":
        if computer=="rock":
            print("computer:",computer)
            print("player:",player)
            print("you lose:(")
        if computer=="paper":
            print("computer:",computer)
            print("player:",player)
            print("you win!!")

    play_again=input("wanna play again? if yes enter yes or no:").lower()
    if play_again!="yes":
        break
print("byeeeee!")

