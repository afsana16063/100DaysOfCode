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

#Write your code below this line 👇
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

random_num = random.randint(0,2)
game_images = [rock, paper, scissors]

print(f"Your choice:\n{game_images[user_choice]}\n")
print(f"Computer choice:\n{game_images[random_num]}")


if random_num == user_choice:
    print("Its a draw")
elif random_num == 0 and user_choice == 1:
    print("You win")
elif random_num == 0 and user_choice == 2:
    print("You lose")
elif random_num == 1 and user_choice == 2:
    print("You win")
elif random_num == 1 and user_choice == 0:
    print("You lose")
elif random_num == 2 and user_choice == 0:
    print("You win")
elif random_num == 2 and user_choice == 1:
    print("You lose")
elif user_choice > 2 or user_choice < 0:
    print("invalid number")







