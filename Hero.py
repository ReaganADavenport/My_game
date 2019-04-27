from Character import Character
from Warrior import Warrior

class Hero(Warrior):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.points = 0

#a variant of attack that adds 10 more power to the player
    def use_pen(self, enemy):
        enemy.health = enemy.health - (self.power + 10)
        if enemy.alive() != True:
            self.points = self.points + 40
            self.health = self.health + 5
            self.power = self.power + 5

#a variation on the Warrior.attack() method that adds points for every enemy killed

    def hero_attack(self, enemy):
        Warrior.attack(self, enemy)
        if enemy.alive() != True:
            self.points = self.points + 20
            self.health = self.health + 5
            self.power = self.power + 5
            return self.points, self.health, self.power
            
#a method to return the number of points the player has earned

    def point_calculator(self):
        return self.points

#a mechanic to gain back health

    def eat(self, food):
        self.health = self.health + 5
        return self.health
    