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

import codecs
import random

list_of_hand_signs = [rock, paper, scissors]

playerSelection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if playerSelection == 0:
    playerSelection = list_of_hand_signs[0]
elif playerSelection == 1:
    playerSelection = list_of_hand_signs[1]
else:
    playerSelection = list_of_hand_signs[2]

print(f"Player Chose: {playerSelection}")

computerSelection = random.choice(list_of_hand_signs)
print(f"Computer Chose: {computerSelection}")

#Rock Paper Scissors 
#- Rock wins against scissors
#- Scissors win against paper
#- Paper wins against rock 

if playerSelection == computerSelection:
    print("It's a draw!")
elif playerSelection == list_of_hand_signs[0] and computerSelection == list_of_hand_signs[2]:
    print("Rock Breaks Scissors, Player Wins!")
elif playerSelection == list_of_hand_signs[1] and computerSelection == list_of_hand_signs[0]:
    print("Paper covers Rock, Player Wins!")
elif playerSelection == list_of_hand_signs[2] and computerSelection == list_of_hand_signs[1]:
    print("Scissors cut Paper, Player Wins!")
else: 
    print("Computer Wins!")