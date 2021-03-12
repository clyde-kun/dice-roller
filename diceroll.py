import random

state = "reroll"
#x variable is set up for a future instance
x = "y"

while state == "reroll":
    
    #here x is used as a deciding factor wheter or not to take user input again
    if x == "y":
        user = input('────────────────────────────────────────────────\ntype "roll"\n────────────────────────────────────────────────\n' )

    value = random.randint(1, 6)

    if user == "roll":
        if value == 1:
            print("────────────────────────────────────────────────\nX\n────────────────────────────────────────────────────────────────────────────────────────────────\n")
        if value == 2:
            print("────────────────────────────────────────────────\nXX\n────────────────────────────────────────────────────────────────────────────────────────────────\n")
        if value == 3:
            print("────────────────────────────────────────────────\nXXX\n────────────────────────────────────────────────────────────────────────────────────────────────\n")
        if value == 4:
            print("────────────────────────────────────────────────\nXXXX\n────────────────────────────────────────────────────────────────────────────────────────────────\n")
        if value == 5:
            print("────────────────────────────────────────────────\nXXXXX\n────────────────────────────────────────────────────────────────────────────────────────────────\n")
        if value == 6:
            print("────────────────────────────────────────────────\nXXXXXX\n────────────────────────────────────────────────\n")
    
        state = input('Type reroll to roll again or click enter to exit\n────────────────────────────────────────────────\n')
        
        #/*in this if statement x is set to a different value than previously in order to make program let user reroll the dice by simply typing "reroll" rather than having to type
        # reroll and roll
        if state == "reroll":
            user = "roll"
            x = "x"