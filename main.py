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
print("What do you choose? ROCK, PAPER, or SCISSORS?\n")
my_choice = input()
if my_choice == "ROCK":
    print(rock)
elif my_choice == "PAPER":
    print(paper)
else:
    print(scissors)

print("Devrabot chose:\n")
li = [rock, paper, scissors]
devrabot_choice = random.choice(li)
print(devrabot_choice)

if my_choice == "ROCK" and devrabot_choice == scissors:
    print("You win!")
elif my_choice == "ROCK" and devrabot_choice == paper:
    print("You lose!")
elif my_choice == "ROCK" and devrabot_choice == rock:
    print("Tie!")
    
elif my_choice == "PAPER" and devrabot_choice == rock:
    print("Pfft. You lose!")
elif my_choice == "PAPER" and devrabot_choice == scissors:
    print("Pfft. You lose!")
elif my_choice == "PAPER" and devrabot_choice == paper:
    print("Tie!")
    
elif my_choice == "SCISSORS" and devrabot_choice == paper:
    print("You win!")
elif my_choice == "SCISSORS" and devrabot_choice == rock:
    print("Pfft. You lose!")
elif my_choice == "SCISSORS" and devrabot_choice == scissors:
    print("Tie!")
    
