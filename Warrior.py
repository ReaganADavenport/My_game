from Character import Character

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