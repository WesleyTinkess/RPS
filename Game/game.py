print("Welcome to Rock-Paper-Scissors!")


choice = input("Choose rock, paper, or scissors: ")
print(f"You chose: {choice}")

import random
options = {1:"Rock", 2:"Paper", 3:"Scissors"}
computer_choice = random.randint(1,3)
print(f"Computer chose {options[computer_choice]}")