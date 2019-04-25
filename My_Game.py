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
        #self.points = points
        self.points = 0
        self.inventory = []

    def magic(self, other_person):
        other_person.health = other_person.health - self.power

    def point_calculator(self, other_person):
        if other_person.alive() == False:
            self.points = self.points + 20

    def take(self, item):
        self.inventory.append(item)

    def get_inventory(self):
        print(self.inventory)    
            

class Civilian(Character):
    pass

class Monster(Warrior):
    pass    


kat = Hero('Kat', 20, 10)
goblin = Monster('Gobby', 10, 2)


def main():
    kat.attack(goblin)
    kat.print_status()
    kat.get_inventory()
    katherine.point_calculator(goblin)
    print(points)

main()    