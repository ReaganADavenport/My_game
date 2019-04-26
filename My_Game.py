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
    elif user_input == "2":
        game_on = False
        print("Nooooooo =(")      
    
    while game_on == True:
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
    elif user_input == "2":
        game_on = False
        print("Nooooooo =(")      
    
    while game_on == True:
        print()
        print("Oh no! A giant snail is trying to take your pen!")
        print("What is your next move?")
        print("1. Fight with your fists")
        print("2. Do nothing")
        print("3. Run away")
        user_input1 = input(">>")
        while big_snail.alive():
            if user_input1 == "1":
                vasa.hero_attack(big_snail)
                big_snail.print_status()
                big_snail.attack(vasa)
                vasa.print_status()
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
        print()
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
    
#Player changes locations

#Forest
        print("Welcome to the Evil Forest!")
        print("It's awfully quiet around here...")
        print("What to do, what to do?")
        print("1. Fight")
        print("2. Look around")
        print("3. Nothing")
        user_input3 = input(">>")
        if user_input3 == "1":
            print("You're fighting air.")
        elif user_input3 == "2":
            print("There is a goblin right in front of you!")
            print("What are you going to do now?")
            print("1. Fight")
            print("2. Run back to where you came from")
            user_input4 = input(">>")
            while goblin1.alive():
                if user_input4 == "1":
                    vasa.hero_attack(goblin1)
                    vasa.print_status()
                    goblin1.print_status()
                    if goblin1.alive() == False:
                        print("The goblin is dead!")
                elif user_input4 == "2":
                    print()
                    print("You ran into a black hole!")
                    break
                elif user_input4 == "3":
                    print()
                    print("Goodbye!")
                    break
        print("Would you like to continue on?")
        print("1. Yes")
        print("2. No")
        user_input5 = input(">>")
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
            user_input7 = input(">>")
            while cyclops.alive():
                if user_input7 == "1":
                    vasa.hero_attack(cyclops)
                    cyclops.print_status()
                    vasa.print_status()
                    if cyclops.alive == False:
                        print()
                        print("You killed the cylcops!")
                elif user_input7 == "2":
                    print("You got eternally lost at Malevolent Mountains")
                    break
                elif user_input6 == "3":
                    print("Welp! Game Over")
                    break

        print("Would you like to continue on?")
        print("1. Yes")
        print("2. No")
        user_input8 = input(">>")
        if user_input8 == '1':
            print()
            print("Let's go to the Tower of the Evil Wizard!")
        elif user_input8 == '2':
            print()
            print("Okay, bye!")
            break 

    #Go to the tower of the evil wizard

main() 
 