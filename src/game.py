from models import Monster, Character
from utils import get_random_monster
import random

def combat_turn(team : list[Character], monster : Monster):
    for c in team:
        if c.is_alive():
            if fight_monster(c, monster):
                print("The monster has been defeated")
                return True
    selected_c = monster_fight_character(monster, team)
    if not selected_c.is_alive() :
        print(f"The {selected_c.name} has been defeated")

def monster_fight_character(monster : Monster, team : list[Character]):
    c = random.choice(team)
    monster.attack_target(c)
    return c

def fight_monster(character : Character, monster : Monster):
    character.attack_target(monster)
    return monster.is_alive()

def start_combat(team : list[Character], db):
    wave = 1
    while any(char.is_alive() for char in team):
        combat_turn(team, get_random_monster(db))
        wave += 1
    return wave