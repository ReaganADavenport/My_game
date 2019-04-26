from Character import Character
from Warrior import Warrior   
from Hero import Hero    
from Monster import Monster       

vasa = Hero('Vasalisa', 20, 10)
wizard = Monster('The Evil Wizard', 90, 16)
big_snail = Monster('Nigel, the giant snail', 15, 2)
goblin1 = Monster('Gobby, the goblin', 10, 4)
goblin2 = Monster('Dobby, the goblin', 10, 4)
troll = Monster('Bert, the troll', 20, 6)
cyclops = Monster('Ted, the cyclops', 20, 9)



def main():
    print("Welcome Sorceress Vasalisa!")
    print("The evil wizard has come and he's terrorizing everyone!")
    print("We need you to help us!")
    print("Are you ready to start?")
    print('1. Yes')
    print('2. No')
    user_input = input(">>")
    if user_input == "1":
        game_on = True
        print()
        print("Great! You have now arrived at Snail Village. Make sure you keep your Magic Pen handy.")
        #ascii village
        print("            |   _   _")
        print("      . | . x .|.|-|.|")
        print("   |\ ./.\-/.\-|.|.|.|")
        print("~~~|.|_|.|_|.|.|.|_|.|~~~")
    elif user_input == "2":
        game_on = False
        print("Nooooooo =(")      
    
    while game_on == True:
        print()
        print("Oh no! Nigel, the giant snail is trying to take your pen!")
        #ascii snail
        print("     .----.   @   @ ")
        print("   / .-\"-.`.   \ /")
        print("   | | ('\ \ \_/ )")
        print("  ,-\ `-.' /.'  /")
        print(" '---`----'----'")
        print("What is your next move?")
        print("1. Fight with your fists")
        print("2. Do nothing")
        user_input1 = input('>>')
        while big_snail.alive():
            if user_input1 == "1":
                vasa.hero_attack(big_snail)
                if big_snail.alive() == False:
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
        print()
        print(" ^  ^   ^  ^  ^   ^  ^")
        print("/|\/|\ /|\/|\/|\ /|\/|\ ")
        print("/|\/|\ /|\/|\/|\ /|\/|\ ")
        print("/|\/|\ /|\/|\/|\ /|\/|\ ")
        print()
        print("It's awfully quiet around here...")
        print("What to do, what to do?")
        print("1. Fight")
        print("2. Look around")
        print("3. Run away")
        print("4. Nothing")
        user_input3 = input(">>")
        if user_input3 == "1":
            print()
            print("You're fighting air.")
        elif user_input3 == "2":
            print()
            print("Gobby, the goblin is right in front of you!")
        #Goblin ascii
        print()
        print("|\  \/      \/  /|")
        print("| \ / =.  .= \ / |")
        print("\( \   o\/o   / )/")
        print(" \_, '-/  \-' ,_/")
        print("   /   \__/   \  ")
        print("   \,___/\___,/  ")
        print(" ___\ \|--|/ /___")
        print("     \      /    ")
        print("      '----'       ")
        print()
        print("What are you going to do now?")
        print("1. Fight")
        print("2. Run back to where you came from")
        user_input4 = input(">>")
        while goblin1.alive():
            if user_input4 == "1":
                vasa.hero_attack(goblin1)
                goblin1.print_status()
                vasa.print_status()
                if goblin1.alive() == False:
	                print("Gobby is dead!")
            elif user_input4 == "2":
                print()
                print("You ran into a black hole!")
                break
            elif user_input3 == "3":
                print()
                goblin1.attack(vasa)
                vasa.print_status()
                goblin1.print_status()  
            elif user_input3 == "4":
                print()
                print("Okay. Bye!")
                break
        
        print("Oh wait! Gobby's brother Dobby is coming after you!")
	        #Goblin ascii
        print()
        print("|\  \/      \/  /|")
        print("| \ / =.  .= \ / |")
        print("\( \   o\/o   / )/")
        print(" \_, '-/  \-' ,_/")
        print("   /   \__/   \  ")
        print("   \,___/\___,/  ")
        print(" ___\ \|--|/ /___")
        print("     \      /    ")
        print("      '----'       ")
        print()
        print("What are you going to do now?")
        print("1. Fight")
        print("2. Nothing")
        print("3. Run back to where you came from")
        user_input5 = input(">>")
        while goblin2.alive():
            if user_input5 == "1":
                print()
                vasa.hero_attack(goblin2)
                if goblin2.alive() == False:
                    print("Dobby is dead!")
            elif user_input5 == "2":
                print()
                goblin2.attack(vasa)
                vasa.print_status()
                goblin2.print_status()
            elif user_input5 == "3":
                print()
                print("You ran into a black hole!")
                break
        print()
        print("You look hungry.")
        print("There's plenty of fruits in the forest to eat.")
        print("Oh look! An apple. You could use the energy!")
        
        vasa.eat("apple")
        vasa.print_status()

        print("Yum, just what you needed")
        print()
        print("Would you like to continue on?")
        print("1. Yes")
        print("2. No")
        user_input6 = input(">>")
        if user_input6 == '1':
            print()
            print("Let's go to the Malevolent Mountains!")
        elif user_input6 == '2':
            print()
            print("Okay, bye!")
            break    
	#Mountains
	
        print("Welcome to Malevolent Mountains!")
	        #Mountain ascii
        print()
        print("   /\    /\  /\      /\            /\/\/\  ")
        print("  /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \ ")
        print(" /    \ \  /    \/ /   /  \/  \/  \  /    \   ")
        print("/      \  /     /          \ ")
        print()
        print("What do you want to do?")
        print("1. Walk around.")
        print("2. Look around.")
        print("3. Nothing.")
        print("4. Run away.")
        user_input7 = input(">>")
        if user_input7 == "1":
            print()
            print("Oops! You fell in a ditch!")
            #break
        if user_input7 == "2":
            print()
            print("OMG a cyclops!")
        # Cyclops ascii
        print()
        print(" __,='`````'=/__")
        print(" '//   ( O ) \ `' ")
        print("//|     ,_)   (`\ ")
        print("~~~\  `'==='  /-, ")
        print("      `----'     `")
        print()
        print("What should you do now?")
        print("1. Fight") 
        print("2. Run Away!")
        user_input8 = input(">>")
        if user_input8 == "1":
            print()
            vasa.hero_attack(cyclops)
            if cyclops.alive() == False:
                print("You killed the cylcops!")
        elif user_input8 == "2":
            print()
            print("You got eternally lost at Malevolent Mountains")
            break
        elif user_input8 == "3":
            print()
            cyclops.attack(vasa)
            vasa.print_status()
            cyclops.print_status()
        if user_input8 == "4":
            print()
            print("Welp! Game Over")
            break

        print()
        print("Would you like to continue on?")
        print("1. Yes")
        print("2. No")
        user_input9 = input(">>")
        if user_input9 == '1':
            print()
            print("Let's go to the Tower of the Evil Wizard!")
        elif user_input9 == '2':
            print()
            print("Okay, bye!")
            break 
	
	    #Go to the tower of the evil wizard
	
        print("You have arrived at the Tower of the Evil Wizard...")
        #Tower ascii

        print()
        print('     |>>>')
        print('     |')
        print(' _  _|_  _')
        print('|;|_|;|_|;|')
        print('\.     .  /')
        print(' \:  .   /')
        print('  ||:   |')
        print('  ||:.  |')
        print('  ||:  .|')
        print('  ||:   |')
        print('  ||: , |')
        print('  ||:   |')
        print('  ||: . |')
        print('__||_   |')
        print()

        print("Wizard: Hahahaha! You think you have what it takes to defeat me?!")
        #Wizard ascii
        print()
        print(" |\          .(' *) ' .")
        print(" | \        ' .*) .'*")
        print(" |(*\      .*(// .*) .")
        print(" |___\       // (. '*")
        print(" (((\"'\     // '  * .")
        print(" ((c'7')   //)")
        print(" ((((^))  /  |")
        print("-')))(((-'/")
        print(" (((()) __/'")
        print("  )))( |")
        print("  (()")
        print()
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
                print()
                vasa.hero_attack(wizard)
                #wizard.print_status()
                #vasa.print_status()
                if wizard.alive() == False:
                    print("You killed the evil wizard and saved us!!!!")
                    print("You have %d points!!!!!!" % (vasa.point_calculator() ))
                    game_on = False
                    break
            elif user_input10 == "2":
                print()
                vasa.use_pen(wizard)
                #wizard.print_status()
                #vasa.print_status()
                if wizard.alive() == False:
                    print("You killed the evil wizard and saved us!!!!")
                    print("You have %d points!!" % (vasa.point_calculator() ))
                    game_on = False
                    break
            elif user_input10 == "3":
                print()
                wizard.attack(vasa)
                #vasa.print_status()
                #wizard.print_status()
            elif user_input10 == "4":
                print()
                print("Game over!")
                break

main() 
 