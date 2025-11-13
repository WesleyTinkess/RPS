print("Welcome to Rock-Paper-Scissors!")


import random
options = {1:"Rock", 2:"Paper", 3:"Scissors"}
computer_choice = random.randint(1,3)
print(f"Computer chose {options[computer_choice]}")