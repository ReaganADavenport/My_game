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
    print('1. cyclops')
    print("2. goblin")
    print('3. wizard')
    print("4. snail")
    print("5. troll")
    user_imput = input()
    if user_imput == "1":
        print("there is a big ugly cyclops in front of Vasalisa")
        print(".-'  ____  `-.")
        print("( ( (_()_)  ) ")
        print("`-.   ^^   .-'")
        print("   `._==_.'")
        print("    __)(___)" )


    elif user_imput == "2":
        print("There is an ugly goblin in front of Vasalisa")
        print("|\  \/      \/  /|")
        print("| \ / =.  .= \ / |")
        print("\( \   o\/o   / )/")
        print(" \_, '-/  \-' ,_/")
        print("   /   \__/   \  ")
        print("   \,___/\___,/  ")
        print(" ___\ \|--|/ /___")
        print("     \      /    ")
        print("      '----'       ")

    elif user_imput == "3":
        print("The Evil Wizard stand before Vasalisa")
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

    elif user_imput == "4":
        print("There is a giant snail in front of Vasalisa")
        print("     .----.   @   @ ")
        print("   / .-\"-.`.   \ /")
        print("   | | ('\ \ \_/ )")
        print("  ,-\ `-.' /.'  /")
        print(" '---`----'----'")

    elif user_imput == '5':
        print("There is an ugly troll in front of Vasalisa")
        print(" __,='`````'=/__")
        print(" '// (o) \(o) \ `' ")
        print("//|     ,_)   (`\ ")
        print("~~~\  `'==='  /-, ")
        print("      `----'     `")    

  

main()    