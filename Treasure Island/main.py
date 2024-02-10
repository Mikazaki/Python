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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
lr = input('You have arrived at a crossroad. Where do you want to? "Left" or "Right"\n')
lrr = lr.lower()
if lrr == "right":
    bs = input("You've come to lake. There is an island in the middle of the lake."' Type "Wait" to wait for a boat. Type "Swim" to swim across.\n')
    bss = bs.lower()
    if bss == "wait":
        print("\nCongratulations, you have evolved from being a dumbass to dumbo. If ya have chosen swim, then the crocodiles in the lake would have ripped ur balls out.")
        cl = input("\nWell now you have arrived at the island, with balls intact might I add, There is a cave with 4 stone doors. One White, one Black, one Red and Yellow. Which door do you choose dumbo?\n")
        cll = cl.lower()
        if cll == "white":
          print("You racist bastard, you believe in white supremacy don't you. You think the whites have the treasure."' YOU HAVE BEEN KILLED BY A "MENTALLY ILL" WHITE GUY.')
        elif cll == "black":
          print("You racist piece of shit. YOU HAVE BEEN STABBED TO DEATH!")
        elif cll == "red":
          print("BURN U RACIST BASTARD!")
        else:
          print("I know you have typed either black or white or both before yellow. If ya havent well dont mind it. You get your treasure. And if you have, well since ya made it here, might as well take it.")
    else:
      print("Sigh, not only are you a dumbass, but now you a are dumbass with no balls. YOU ARE DEAD!")
else:
    print('YOU ARE DEAD. Dumbass, the word "Right" indicates the "right way". Suck ass BOZO.')
