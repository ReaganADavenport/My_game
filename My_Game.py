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
    goblin1.attack(vasa)
    vasa.hero_attack(goblin1)
    vasa.print_status()
    goblin1.print_status()
    vasa.take('Loot')
    vasa.get_inventory()
    vasa.point_calculator()

    vasa.eat('apple')
    vasa.print_status()

main()    