from models import Monster, Character
from utils import get_random_monster
from abilities import execute_ability
import random

def print_monster_status(monster):
    print(f"Monstre: {monster.name} ({monster.current_hp}/{monster.max_hp} points de vie)")

def team_attacks_monster(team, monster):
    for c in team:
        if c.is_alive():
            is_crit = c.attack_target(monster)
            crit_text = " COUP CRITIQUE!" if is_crit else ""
            print(f"{c.name} : {c.current_hp}/{c.max_hp} attaque {monster.name}{crit_text}")

def print_team_status(team):
    print("\nÉtat de l'équipe:")
    for c in team:
        if c.is_alive():
            cooldown_text = f" [{c.ability_name}: pret]" if c.is_ability_ready() else f" [{c.ability_name}: {c.current_cooldown} tours]"
            print(f"  {c.name}: {c.current_hp}/{c.max_hp} HP{cooldown_text}")

def ask_ability_usage(character):
    if not character.is_ability_ready():
        return False

    response = input(f"{character.name} peut utiliser {character.ability_name}. Utiliser? (o/n): ").lower()
    return response == 'o'

def reduce_team_cooldowns(team):
    for c in team:
        if c.is_alive():
            c.reduce_cooldown()

def handle_abilities(team, monster):
    for c in team:
        if c.is_alive() and ask_ability_usage(c):
            execute_ability(c, team, monster)
            if not monster.is_alive():
                return True
    return False

def combat_turn(team : list[Character], monster : Monster):
    print("\nTour de combat")
    print_monster_status(monster)

    if handle_abilities(team, monster):
        print("Le monstre a ete vaincu")
        reduce_team_cooldowns(team)
        return True

    team_attacks_monster(team, monster)

    if not monster.is_alive():
        print("Le monstre a ete vaincu")
        reduce_team_cooldowns(team)
        return True

    selected_c = monster_fight_character(monster, team)
    if not selected_c.is_alive():
        print(f"{selected_c.name} a ete vaincu")

    print_team_status(team)
    reduce_team_cooldowns(team)
    return False

def monster_fight_character(monster : Monster, team : list[Character]):
    c = random.choice(team)
    is_crit = monster.attack_target(c)
    crit_text = " COUP CRITIQUE!" if is_crit else ""
    print(f"Monstre : {monster.name} attaque {c.name} ({c.current_hp}/{c.max_hp} points de vie){crit_text}")
    return c

def is_team_alive(team):
    return any(char.is_alive() for char in team)

def fight_monster(team, monster):
    while monster.is_alive() and is_team_alive(team):
        if combat_turn(team, monster):
            break

    return is_team_alive(team)

def start_combat(team : list[Character], db):
    wave = 0

    while is_team_alive(team):
        wave += 1
        monster = get_random_monster(db)
        print(f"\nVague {wave} - {monster.name} apparait!")

        if not fight_monster(team, monster):
            break

    return wave - 1 if wave > 0 else 0