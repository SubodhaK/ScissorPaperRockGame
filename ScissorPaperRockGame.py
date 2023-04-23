# This Is Scissor Paper Rock Game  
"ramdom module is use to take random values from computer"
import random


helpingYou = input("if you want help menu type y, if you don't type n  ")

gameHelp = """
###############################################################################################################################################################################

The game consists of a certain number of rounds, which is decided by the user at the beginning of the game.

The player and the computer each select one of three options: "scissor", "paper", or "rock".

The winner of each round is determined by the following rules:

Scissor beats paper
Paper beats rock
Rock beats scissor

If both the player and the computer choose the same option, the round is a draw and no points are awarded.

After each round, the score is displayed and the game moves on to the next round.

At the end of the game, the final score is displayed and the winner is declared.

To play the game, simply input your choice (either "scissor", "paper", or "rock") when prompted, and the program will automatically generate the computer's choice.
Enjoy the game!

##############################################################################################################################################################################
"""
if helpingYou == "y":
    print(gameHelp)


palyerMarks = 0
ComputerMarks = 0
HowManyRounds = int(input("how many rounds you need?  "))



choises = ["scissor","paper","rock"]


# this is the computer choise

for GameRound in range(HowManyRounds):
    computer = random.choice(choises)
    print("")
    print("*"*10)
    player = input("what is your choise?  ")
    print("")
    print(f"This is the {GameRound + 1} round")
    print("#"*10)
    print(f"your - {player}")
    print("#"*10)
    print(f"computer - {computer}")
    print("#"*10)
    
    if player in choises:      
        if player == choises[0] and computer == choises[0]:
            print(f"round {GameRound +1} is draw go to next round" )
            GameRound += 1
        elif player == choises[0] and computer ==choises[1]:
            palyerMarks += 1
            print(f"yheee !!!! you win round {GameRound +1}, go next round")
            GameRound += 1
        elif player == choises[0] and computer == choises[2]:
            ComputerMarks += 1
            print(f"ohh you loss round {GameRound +1}, go next round ")
            GameRound += 1

        elif player == choises[1] and computer == choises[0]:
            ComputerMarks += 1
            print(f"ohh you loss round {GameRound +1}, go next round ")
            GameRound += 1

        elif player == choises[1] and computer == choises[1]:
            print(f"round {GameRound +1} is draw go to next round" )
            GameRound += 1

        elif player == choises[1] and computer ==choises[2]:
            palyerMarks += 1
            print(f"yheee !!!! you win round {GameRound +1}, go next round")
            GameRound += 1

        elif player == choises[2] and computer ==choises[0]:
            palyerMarks += 1
            print(f"yheee !!!! you win round {GameRound +1}, go next round")
            GameRound += 1

        elif player == choises[2] and computer == choises[1]:
            ComputerMarks += 1
            print(f"ohh you loss round {GameRound +1}, go next round ")
            GameRound += 1

        else:
            print(f"round {GameRound +1} is draw go to next round" )
            GameRound += 1    
    else:
        print("enter valid choice")

print("")
print("Game Is end now")
if palyerMarks > ComputerMarks:
    print("You are win")
else:
    print("you loss")
print("*"*10)    
