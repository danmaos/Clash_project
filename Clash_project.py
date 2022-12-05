import time

class Character:
    def __init__(self, name, hp, aps, dmg):
        self.name = name
        self.hp = hp
        self.aps = aps
        self.dmg = dmg

class Str(Character):
    def __init__(self, name, hp, aps, dmg, hpreg):
        super().__init__(name, hp, aps, dmg)
        self.hpreg = hpreg

class Agi(Character):
    def __init__(self, name, hp, aps, dmg, armour):
        super().__init__(name, hp, aps, dmg)
        self.armour = armour

char1 = Str("Warrior", 5000, 1, 1000, 200)
char2 = Agi("Archer", 2500, 4, 300, 500)

def ring():
    while char1.hp > 0 and char2.hp > 0:
        char1.hp = char1.hp - (char2.aps * char2.dmg) + char1.hpreg
        char2.hp = char2.hp - (char1.aps * char1.dmg - char2.armour)
        print(char1.name + "'s health is", char1.hp)
        print(char2.name + "'s health is", char2.hp)
        time.sleep(1)
    if char1.hp > char2.hp:
        return print("Winner is", char1.name)
    elif char1.hp < char2.hp:
        return print("Winner is", char2.name)
    else:
        return print("Draw")

ring()