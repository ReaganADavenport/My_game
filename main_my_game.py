def main():

    vasa.hero_attack(goblin)
    vasa.print_status()
    goblin.print_status()
    vasa.take('Loot')
    vasa.get_inventory()
    vasa.point_calculator()

    print("Welcome Sorceress Vasalisa!")
    print("The evil wizard has come and he's terrorizing everyone!")
    print("We need you to help us!")
    print("Are you ready to start?")
    
    user_input = input("Yes or no? ")
    if user_input.lower() == ("yes"):
        print("Great! You have now arrived at Snail Village. Make sure you keep your Magic Pen handy.")
    elif user_input.lower() == ("no"):
        print("Nooooooo =(")        
    
#Village

    print("Oh no! A giant snail is trying to take your pen!")
    print("What is your next move?")
    print("1. Fight with your fists")
    print("2. Do nothing")
    print("3. Run away")
    user_input1 = input()
    if user_input1 == "1":
        vasa.hero_attack(big_snail)
        if big_snail.health <= 0
        print("The giant snail is dead!")
    elif user_input1 == "2":
        pass
    elif user_input1 == "3":
        print("You're dead")

    print("Now, let's go to ___")
    
#Player changes locations

#Forest
    print("Welcome to Evil Forest!")
    print("It's awfully quiet around here...")
    print("What to do, what to do?")
    print("1. Fight")
    print("2. Look around")
    print("3. Nothing")
    user_input2 = input()
    if user_input2 == "1":
        print("You're fighting air!")
    if user_input2 == "2":
        print("There is a big snail right in front of you!")
        print("What are you going to do now?")
        print("1. Fight")
        print("2. Run back to where you came from")
            user_input3 = input()
            if user_input3 == "1":
                vasa.hero_attack(big_snail)
                if big_snail.health <= 0
                print("The giant snail is dead!")
            elif user_input3 == "2":
                print("You ran into a black hole!")
    if user_input2 == "3":
        print("Goodbye!")
    
#Mountains

    print("Welcome to Malevolent Mountains!")
    print("What do you want to do?")
    print("1. Walk around.")
    print("2. Look around.")
    print("3. Nothing.")
    user_input4 = input()
    if user_input4 == "1":
        print("Oops! You fell in a ditch!")
    if user_input4 == "2":
        print("OMG a cyclops!")
        #Cyclops ascii
        print("What should you do now?")
        print("1. Fight")
        print("2. Run Away!")
            user_input5 = input()
            if user_input5 == "1":
                vasa.hero_attack(cyclops)
                if cyclops.health <= 0
                print("You killed the cylcops!")
            if user_input5 == "2":
                print("You got eternally lost at Malevolent Mountains")
    if user_input4 == "3":
        print("Welp! Game Over")



main()