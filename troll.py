# Game Over version 2
# Demonstrate while loop - evaluate until we run out
# R.M. 12-12-20

# introduction to the game
print("Your Hero is surrounded by an army of trolls")
print("Your Hero begins the fight by unleashing his sword: ")
print("Your Hero gets x health and y number of swipes with his sword\n")

health = 10
trolls = 0
damage = 3

while health >= 0:
    trolls += 1
    health = health - damage

    print("Your hero swipes and kills a troll, "\
          "but takes damage", damage, "damage points.\n")

print("your hero fought bravely, and defeated", trolls, "trolls")
print("but the game is rigged so we are perpetual losers ..........")

# exit program
input("Press enter key to get out of program")
