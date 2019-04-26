def main():
    print("Welcome Sorceress Vasalisa!")
    print("The evil wizard has come and he's terrorizing everyone!")
    print("We need you to help us!")
    print("Are you ready to start?")
    print("1. Yes")
    print("2. No")
    user_input = input()
    if user_input == "1":
        game_on = True
        print("Great! You have now arrived at Snail Village. Make sure you keep your Magic Pen handy.")
    elif user_input == "2":
        game_on = False
        print("Nooooooo =(")
        break        
    
#Village
    while game_on == True:
        print("Oh no! A giant snail is trying to take your pen!")
        print("What is your next move?")
        print("1. Fight with your fists")
        print("2. Do nothing")
        print("3. Run away")
        user_input1 = input()
        if user_input1 == "1":
            vasa.hero_attack(big_snail)
            if big_snail.alive() == False:
                print("The giant snail is dead!")
                vasa.print_status()
        elif user_input1 == "2":
            big_snail.attack(vasa)
            vasa.print_status()
            big_snail.print_status()
        elif user_input1 == "3":
            print("You're dead")
            break

        print("Would you like to continue on?")
        print("1. Yes")
        print("2. No")
        user_input2 = input()
        if user_input2 == '1':
            print("Let's go to the Evil Forest!")
        elif user_input2 == '2':
            print("Okay, bye!")
            break 
    
#Player changes locations

#Forest
        print("Welcome to the Evil Forest!")
        print("It's awfully quiet around here...")
        print("What to do, what to do?")
        print("1. Fight")
        print("2. Look around")
        print("3. Nothing")
        user_input3 = input()
        if user_input3 == "1":
            print("You're fighting air.")
        elif user_input3 == "2":
            print("There is a big snail right in front of you!")
            print("What are you going to do now?")
            print("1. Fight")
            print("2. Run back to where you came from")
                user_input4 = input()
                if user_input4 == "1":
                    vasa.hero_attack(big_snail)
                    if big_snail.alive() == False:
                        print("The giant snail is dead!")
                elif user_input4 == "2":
                    print("You ran into a black hole!")
                    break
                elif user_input4 == "3":
                    print("Goodbye!")
                    break
        print("Would you like to continue on?")
        print("1. Yes")
        print("2. No")
        user_input5 = input()
        if user_input5 == '1':
            print("Let's go to the Malevolent Mountains!")
        elif user_input5 == '2':
            print("Okay, bye!")
            break    
#Mountains

        print("Welcome to Malevolent Mountains!")
        print("What do you want to do?")
        print("1. Walk around.")
        print("2. Look around.")
        print("3. Nothing.")
        user_input6 = input()
        if user_input6 == "1":
            print("Oops! You fell in a ditch!")
        if user_input6 == "2":
            print("OMG a cyclops!")
        #Cyclops ascii
            print("What should you do now?")
            print("1. Fight")
            print("2. Run Away!")
                user_input7 = input()
                if user_input7 == "1":
                    vasa.hero_attack(cyclops)
                    if cyclops.alive == False:
                        print("You killed the cylcops!")
                elif user_input7 == "2":
                    print("You got eternally lost at Malevolent Mountains")
                    break
        if user_input6 == "3":
            print("Welp! Game Over")
            break

        print("Would you like to continue on?")
        print("1. Yes")
        print("2. No")
        user_input8 = input()
        if user_input8 == '1':
            print("Let's go to the Tower of the Evil Wizard!")
        elif user_input8 == '2':
            print("Okay, bye!")
            break 

    #Go to the tower of the evil wizard

main()