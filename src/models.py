class Entity:
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_hp = hp
        self.current_hp = hp

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense / 2)
        self.current_hp = max(0, self.current_hp - actual_damage)

    def attack_target(self, target):
        target.take_damage(self.attack)

    def get_stats(self):
        return {
            "name": self.name,
            "current_hp": self.current_hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense
        } # Accessible via entity.get_stats()['name']

# Custom classes to separate Characters from Monsters
# In the future, there may be custom methods depending on the class
# But for now they are strictly the same.
class Character(Entity):
    pass

class Monster(Entity):
    pass