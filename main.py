import random
print("Press 'Enter' to continue")
name= input()
user_action= input("Enter a choice R for rock,P for paper or S for scissors; ")
possible_actions= ["R", "P", "S"]
computer_action= random.choice(possible_actions)
print(f"\n You chose {user_action}, computer chose {computer_action}.\n")

while range(1):
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print(f"Rock smashes {name}! You win!")
        else:
            print(f"Paper covers {name}! You lose.")


    elif user_action == "P":
        if computer_action == "R":
            print(f"Paper covers {name}! You win!")
        else:
            print(f"Scissors cuts {name}! You lose.")

    elif user_action == "S":
        if computer_action == "P":
            print(f"Scissors cuts {name}! You win!")
        else:
            print(f"Rock smashes  {name}! You lose.")
    else:
        print("Invalid input,restart game and enter R or P or S")
    break


i=0

while i==0: 
    user_choice= input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break

