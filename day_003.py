print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`.""` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')


print("Welcome to Treasure Island!!!")
print("Your mission is to find the treasure island.")
path = input("Please select left or right path...")

if path.lower() == "left":
      swin = input("You are form a lake, What to do swin or wait? ")
      if swin.lower() == "swin":
            door = input("You are form a three doors Red, Blue or Yellow, choice one? ")
            if door.lower() == "yellow":
                  print("You find the treasure!!!!!")
            elif door.lower() == "blue":
                  print("Eaten by beasts. Game Over...")
            elif door.lower() == "red":
                  print("Burned by fire. Game Over...")
            else:
                  print("Choice a valid door color...")
      else:
            print("Attacked by trout. Game Over...")
else:
      print("Fall into a hole. Game Over...")



