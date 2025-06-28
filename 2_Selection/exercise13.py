player = input("What do you choose: paper, rock or scissors? ")
computer = "paper"
print(f"You chose {player}")

match player:
    case "paper":
        if computer == "paper":
            print("Till")
        elif computer == "rock":
            print("You win :-)")
        elif computer == "scissors":
            print("You lose!")
    case "rock":
        if computer == "paper":
            print("You lose!")
        elif computer == "rock":
            print("Till")
        elif computer == "scissors":
            print("You win :-)")
    case "scissors":
        if computer == "paper":
            print("You win :-)")
        elif computer == "rock":
            print("You lose!")
        elif computer == "scissors":
            print("Till")