import random

# print(round(random.random() * 5, 1))

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

while True:
    human_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    print("Your choose: ")
    if human_choose == 0:
        print(rock)
    elif human_choose == 1:
        print(paper)
    elif human_choose == 2:
        print(scissors)
    else:
        print("Choose again.")

    if human_choose <= 2:
        computer_choose = random.randint(0, 2)
        print("Computer choose: ")
        if computer_choose == 0:
            print(rock)
        elif computer_choose == 1:
            print(paper)
        elif computer_choose == 2:
            print(scissors)

        if human_choose == computer_choose:
            print("It's a tie!")
        elif (human_choose == 0 and computer_choose == 2) or (human_choose == 1 and computer_choose == 0):
            print("You Wins!")
        else:
            print("You Lose!")
