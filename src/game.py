from models import Monster, Character
from utils import get_random_monster
import random

def combat_turn(team : list[Character], monster : Monster):
    print("\nTour de combat")
    print(f"Monstre: {monster.name} ({monster.current_hp}/{monster.max_hp} points de vie)")

    for c in team:
        if c.is_alive():
            print(f"{c.name} : {c.current_hp}/{c.max_hp} attaque {monster.name}")
            if fight_monster(c, monster):
                print("The monster has been defeated")
                return True
            selected_c = monster_fight_character(monster, team)
            if not selected_c.is_alive() :
                print(f"The {selected_c.name} has been defeated")

    print("\nÉtat de l'équipe:")
    for c in team:
        if c.is_alive():
            print(f"  {c.name}: {c.current_hp}/{c.max_hp} points de vie")

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