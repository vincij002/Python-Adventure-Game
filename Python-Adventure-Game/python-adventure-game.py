print(" Welcome to the haunted maze! Remember to type you answers as given inside of the quotations. ")

print(" You find yourself standing at the entrance of an eerie maze in the middle of the night. The moon casts an unsettling glow on the twisted \n hedges that seem to reach out like skeletal fingers. A chilling wind whispers through the narrow pathways, carrying with it a sense of \n foreboding. You have no choice but to navigate through the maze, hoping to reach the other side unscathed.")



choice1 = input(' You stand at the entrance, facing two paths. To the left, the path is dimly lit, with a faint glow in the distance. To the right, the shadows grow darker,\n shrouding the path in mystery. Which way will you choose? Type "left" or "right" \n')
if choice1 == "left":
  choice2 = input('You find yourself in a beautiful garden with a swan fountain. You notice the swans eyes are made of saphires. Do you choose to steal the saphire? \nType "yes" or "no".\n')
  if choice2 == "no":
    choice3 = input('The ghost of the man who maintained the maze appears and is impressed with your choice he has agreed to help you. \nHe offers 3 items to help you escape. A "live grenade", a "jetpack", and finally in exchange for your release the ghost requests your "SSN". Which do you chose? \n')
    if choice3 == "live grenade":
      print("You accepted a live grenade from a ghost? That was not smart, you sadly pass.")
    elif choice3 == "SSN":
      print("The ghost stole your SSN, identity and ruined your credit.")
    elif choice3 == "jetpack":
      print("Congratulations you've escaped the maze!")
    else:
      print("You were indecisive and the ghost lost patients. You're trapped forever.")
  else:
    print("For your thievery you fell into a trap door and you are stuck there for all eternity.")
else:
  print("You walk face first into the maze maybe choose the other direction?")
