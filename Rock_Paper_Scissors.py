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
game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
    print("You typed invalid number,\nYou lose!")
else:
    print(game_images[choice])

computer_chose = random.randint(0,2)
print(f"Computer Choice:\n{game_images[computer_chose]}")

if choice == 0 and computer_chose == 2:
    print("You win!")
elif choice == 2 and computer_chose == 1:
    print("You Win!")
elif choice == 1 and computer_chose == 0:
    print("You Win!")
elif choice == 0 and computer_chose == 1:
    print("You lose!")
elif choice == 2 and computer_chose == 0:
    print("You lose!")
elif choice == 1 and computer_chose == 2:
    print("You lose!")
elif choice == computer_chose:
    print("It's a draw. ")
else:
    print("You typed an invailed number, You lose!")

