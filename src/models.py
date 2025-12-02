
class Character:
    def __init__(self, name, attack, defense, max_hp, current_hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_hp = max_hp
        self.current_hp = current_hp

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, damage):
        self.current_hp -= damage

    def attack_target(self, target):
        target.take_damage(self.attack)

    def get_stats(self):
        return self.current_hp, self.max_hp, self.attack, self.defense

class Monster:
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def attack_player(self, player):
        player.take_damage(self.attack)

    def get_stats(self):
        return self.hp, self.defense