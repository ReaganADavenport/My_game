def main():
	    print("Welcome Sorceress Vasalisa!")
	    print("The Evil Wizard has come and he's terrorizing everyone!")
	    print("We need you to help us!")
	    print("Are you ready to start?")
	    print("1. Yes")
        print("2. No")
        user_input = input(">>")
	    if user_input == "1":
	        game_on = True
	        print("Great! You have now arrived at Snail Village. Make sure you keep your Magic Pen handy.")
	        print("You will need it later to defeat the Evil Wizard")
            ##Village ascii
	    elif user_input == "2":
	        game_on = False
	        print("Nooooooo =(")
	        break        
	
	#Village
	    while game_on == True:
            print()
	        print("Oh no! Nigel, the giant snail is trying to take your pen!")
	        #Snail ascii
	        print("What is your next move?")
	        print("1. Fight with your fists")
	        print("2. Do nothing")
            user_input1 = ('>>')
            while big_snail.alive():
	            if user_input1 == "1":
	                vasa.hero_attack(big_snail)
	                if big_snail.alive() == False:
                        print()
	                    print("Nigel is dead!")
	                    vasa.print_status()
	            elif user_input1 == "2":
	                big_snail.attack(vasa)
                    vasa.print_status()
	            elif user_input1 == "3":
	                print("You're dead")
	                break
	
	        print("Would you like to continue on?")
	        print("1. Yes")
	        print("2. No")
            user_input2 = input(">>")
            if user_input2 == '1':
                print()
                print("Let's go to the Evil Forest!")
            elif user_input2 == '2':
                print()
                print("Okay, bye!")
                break

	#Forest
	        print("Welcome to the Evil Forest!")
	        #Forest ascii
	        print("It's awfully quiet around here...")
	        print("What to do, what to do?")
	        print("1. Fight")
	        print("2. Look around")
	        print("3. Run away")
	        print("4. Nothing")
	        user_input3 = input(">>")
	        if user_input3 == "1":
	            print("You're fighting air.")
	        elif user_input3 == "2":
	            print("Gobby, the goblin is right in front of you!")
	            #Goblin ascii
	            print("What are you going to do now?")
	            print("1. Fight")
	            print("2. Run back to where you came from")
	            user_input4 = input(">>")
                while goblin_1.alive():
	                if user_input4 == "1":
	                    vasa.hero_attack(goblin1)
                        goblin1.print_status()
                        vasa.print_status()
	                    if goblin1.alive() == False:
	                        print("Gobby is dead!")
	                elif user_input4 == "2":
	                    print("You ran into a black hole!")
	                    break
	        elif user_input3 == "3":
	            goblin1.attack(vasa)
	            vasa.print_status()
	            goblin1.print_status()   
	        elif user_input3 == "4":
	            print("Okay. Bye!")
	            break
	
	        print("Oh wait! Gobby's brother Dobby is coming after you!")
	        #Goblin ascii
	        print("What are you going to do now?")
	        print("1. Fight")
	        print("2. Nothing")
	        print("3. Run back to where you came from")
	            user_input5 = input(">>")
                while goblin2.alive():
	                if user_input5 == "1":
	                    vasa.hero_attack(goblin2)
	                    if goblin2.alive() == False:
	                        print("Dobby is dead!")
	                elif user_input5 == "2":
	                    goblin2.attack(vasa)
	                    vasa.print_status()
	                    goblin2.print_status()  
	                elif user_input5 == "3":
	                    print("You ran into a black hole!")
	                    break
	        print()
            print("You look hungry.")
	        print("There's plenty of fruits in the forest to eat.")
	        print("Oh look! An apple. You could use the energy!")
	            vasa.eat("apple")
	            vasa.print_status()
	        print("Yum, just what you needed")
	        print("Would you like to continue on?")
	        print("1. Yes")
	        print("2. No")
	        user_input6 = input(">>")
	        if user_input6 == '1':
	            print("Let's go to the Malevolent Mountains!")
	        elif user_input6 == '2':
	            print("Okay, bye!")
	            break    
	#Mountains
	
	        print("Welcome to Malevolent Mountains!")
	        #Mountain ascii
	        print("What do you want to do?")
	        print("1. Walk around.")
	        print("2. Look around.")
	        print("3. Nothing.")
	        user_input6 = input(">>")
	        if user_input6 == "1":
	        print("3. Runaway")
	        print("4. Nothing.")
	        user_input7 = input(">>")
	        if user_input7 == "1":
	            print("Oops! You fell in a ditch!")
	        if user_input6 == "2":
	        if user_input7 == "2":
	            print("OMG a cyclops!")
	        #Cyclops ascii
	            print("What should you do now?")
	            print("1. Fight")
	            print("2. Run Away!")
	                user_input8 = input(">>")
	                if user_input8 == "1":
	                    vasa.hero_attack(cyclops)
	                    if cyclops.alive == False:
	                        print("You killed the cylcops!")
	                elif user_input8 == "2":
	                    print("You got eternally lost at Malevolent Mountains")
	                    break
	        if user_input6 == "3":
	        elif user_input7 == "3":
	            cyclops.attack(vasa)
	            vasa.print_status()
	            cyclops.print_status()
	        if user_input7 == "4":
	            print("Welp! Game Over")
	            break
	
	        print("Would you like to continue on?")
	        print("1. Yes")
	        print("2. No")
	        user_input9 = input(">>")
	        if user_input9 == '1':
	            print("Let's go to the Tower of the Evil Wizard!")
	        elif user_input9 == '2':
	            print("Okay, bye!")
	            break 
	
	    #Go to the tower of the evil wizard
	
	        print("You have arrived at the Tower of the Evil Wizard...")
        #Tower ascii
        print("Wizard: Hahahaha! You think you have what it takes to defeat me?!")
        #Wizard ascii
        print("I think not! This entire world is mine forever!")
        print("We can do this the easy way or this hard way...the choice is yours. HAHAHAHAHA")
        print("What is your next move?")
        print("1. Fight the evil wizard")
        print("2. Use your magic pen")
        print("3. Runaway")
        print("4. Give up")
        user_input10 = input(">>")
        while wizard.alive():
            if user_input10 == "1":
                vasa.hero_attack(wizard)
                #wizard.print_status()
                #vasa.print_status()
                if wizard.alive() == False:
                    print("You killed the evil wizard and saved us!!!!")
                    print("You have %d points!!!!!!" % (vasa.point_calculator() ))
                    game_on = False
                    break
            elif user_input10 == "2":
                vasa.use_pen(wizard)
                #wizard.print_status()
                #vasa.print_status()
                if wizard.alive() == False:
                    print("You killed the evil wizard and saved us!!!!")
                    print("You have %d points!!" % (vasa.point_calculator() ))
                    game_on = False
                    break
            elif user_input10 == "3":
                wizard.attack(vasa)
                #vasa.print_status()
                #wizard.print_status()
            elif user_input10 == "4":
                print("Game over!")
                break
            
	
main() 
