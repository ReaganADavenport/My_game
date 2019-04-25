class Character:
    def __init__(self, name):
        self.name = name
    

class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name)
        self.health = health
        self.power = power

    def attack(self, other_person):
        other_person.health = other_person.health - self.power

    def print_status(self):
        print('%s has %d health and %d power' % (self.name, self.health, self.power))

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False    
           

class Hero(Warrior):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.points = 0
        self.inventory = ['sword', 'staff']

    def look(self):
        pass

    def use_pen(self, enemy):
        enemy.health = enemy.health - (self.power + 10)


    def hero_attack(self, enemy):
        Warrior.attack(self, enemy)
        if enemy.alive() != True:
            self.points = self.points + 20
            self.health = self.health + 5
            self.power = self.power + 5
            return self.points, self.health, self.power
            

    def magic(self, other_person):
        other_person.health = other_person.health - self.power
        if other_person.alive() != True:
            self.points = self.points + 20
            self.health = self.health + 5
            self.power = self.power + 5
            return self.points, self.health, self.power

    def point_calculator(self):
        print(self.points)

    def eat(self, food):
        self.health = self.health + 5
        return self.health

    def take(self, item):
        self.inventory.append(item)

    def get_inventory(self):
        print(self.inventory)    
            

class Monster(Warrior):
    pass    


vasa = Hero('Vasalisa', 20, 10)
wizard = Monster('The Evil Wizard', 90, 16)
big_snail = Monster('Nigel, the giant snail', 15, 2)
goblin1 = Monster('Gobby, the goblin', 10, 4)
goblin2 = Monster('Dobby, the goblin', 10, 4)
troll = Monster('Bert, the troll', 20, 6)
cyclops = Monster('Ted, the cyclops', 20, 9)



def main():
    vasa.hero_attack(goblin1)
    vasa.print_status()
    goblin1.print_status()
    vasa.take('Loot')
    vasa.get_inventory()
    vasa.point_calculator()

main()    