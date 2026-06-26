import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
strings = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice >= 3:
    print("Invalid input. Please enter 0, 1, or 2.")
else:
    computer_choice = random.randint(0, 2)

    print(f"You chose {strings[user_choice]}\n{game[user_choice]}")
    print(f"Computer chose {strings[computer_choice]}\n{game[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 0):
        print("Computer wins!")
    else:
        print("You win!")