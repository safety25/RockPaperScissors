from random import randint

choice = ["rock" , "paper", "scissors"]


def main():
    computer = choice[randint(0,2)]
    
    print("Welcome to my game!!")
    print("Choose rock-paper-scissors")
    
    player = input ("Your choice: ").lower()
    print("Computer choice: " + computer)
    
    if player == computer:
        print("Draw")
    
    elif player == "rock" and computer == "paper":
        print("Computer wins")
    
    elif player == "rock" and computer == "scissors":
        print("Player wins")
    
    elif player == "paper" and computer == "rock":
        print("Player wins")
    
    elif player == "paper" and computer == "scissors":
        print("Computer wins")
    
    elif player == "scissors" and computer == "rock":
        print("Computer wins")
    
    elif player == "scissors" and computer == "paper":
        print("Player wins")

    
    

main()








