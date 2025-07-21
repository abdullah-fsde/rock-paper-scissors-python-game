import random
def gamewin(Computer,You):
    if Computer == You:
        return None
    elif Computer == "Rock":
        if You == "Paper":
            return True
        elif You == "Scissors":
            return False
    elif Computer == "Paper":
        if You == "Rock":
            return False
        elif You == "Scissors":
            return True
    elif Computer == "Scissors":
        if You == "Rock":
            return True
        elif You == "Paper":
            return False
print("Computers turn...")
number=random.randint(1,3)
if number == 1:
    Computer = "Rock"
elif number == 2:
    Computer = "Paper"
elif number == 3:
    Computer = "Scissors"
print("Your turn to choose")
print('''1.Rock
2.Paper
3.Scissors''')
You = int(input("Enter your choice:"))
if You == 1:
    You = "Rock"
elif You == 2:
    You = "Paper"
elif You == 3:
    You = "Scissors"
print(f"You chose {You}")
print(f"Computer chose {Computer}")
decision = gamewin(Computer,You)
if decision == None:
    print("The game is a tie, Play Again!")
elif decision == True:
    print("You win!")
else:
    print("You lose! Better luck next time")