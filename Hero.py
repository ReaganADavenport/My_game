from Character import Character
from Warrior import Warrior

class Hero(Warrior):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.points = 0
        self.inventory = ['sword', 'staff']


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