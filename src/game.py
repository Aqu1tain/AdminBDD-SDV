from models import Monster, Character
from utils import get_random_monster
import random

def combat_turn(team : list[Character], monster : Monster):
    print("\nTour de combat")
    print(f"Monstre: {monster.name} ({monster.current_hp}/{monster.max_hp} points de vie)")

    for c in team:
        if c.is_alive():
            print(f"{c.name} : {c.current_hp}/{c.max_hp} attaque {monster.name}")
            c.attack_target(monster)

    if not monster.is_alive():
        print("Le monstre a ete vaincu")
        return True

    selected_c = monster_fight_character(monster, team)
    if not selected_c.is_alive():
        print(f"{selected_c.name} a ete vaincu")

    print("\nÉtat de l'équipe:")
    for c in team:
        if c.is_alive():
            print(f"  {c.name}: {c.current_hp}/{c.max_hp} points de vie")

    return False

def monster_fight_character(monster : Monster, team : list[Character]):
    c = random.choice(team)
    print(f"Monstre : {monster.name} attaque {c.name} ({c.current_hp}/{c.max_hp} points de vie)")
    monster.attack_target(c)
    return c

def start_combat(team : list[Character], db):
    wave = 0

    while any(char.is_alive() for char in team):
        wave += 1
        monster = get_random_monster(db)
        print(f"\nVague {wave} - {monster.name} apparait!")

        while monster.is_alive() and any(char.is_alive() for char in team):
            if combat_turn(team, monster):
                break

        if not any(char.is_alive() for char in team):
            break

    return wave - 1 if wave > 0 else 0