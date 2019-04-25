class Character:
    def __init__(self, name):
        self.name = name

class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name)
        self.health = health
        self.power = power

class Hero(Warrior):
    pass

class Civilian(Character):
    pass

class Monster(Warrior):
    pass    

def main():
    while 
