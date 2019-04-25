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
           

class Hero(Warrior):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.points = 0
        self.inventory = ['sword', 'staff']

    def hero_attack(self, enemy):
        Warrior.attack(self, enemy)
        if enemy.alive() != True:
            self.points = self.points + 20
            return self.points

    def magic(self, other_person):
        other_person.health = other_person.health - self.power
        if other_person.alive() != True:
            self.points = self.points + 20
            return self.points

    def point_calculator(self):
        print(self.points)

    def take(self, item):
        self.inventory.append(item)

    def get_inventory(self):
        print(self.inventory)    
            

class Civilian(Character):
    pass

class Monster(Warrior):
    pass    


vasa = Hero('Vasalisa', 20, 10)
goblin = Monster('Gobby', 10, 2)


def main():
    vasa.hero_attack(goblin)
    vasa.print_status()
    goblin.print_status()
    vasa.take('Loot')
    vasa.get_inventory()
    vasa.point_calculator()

main()    