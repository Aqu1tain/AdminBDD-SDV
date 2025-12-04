from models import Monster, Character
from utils import get_random_monster
from abilities import execute_ability
from constants import * # bunch of text and numbers
import random

def print_monster_status(monster):
    print(MSG_MONSTER_STATUS.format(name=monster.name, current_hp=monster.current_hp, max_hp=monster.max_hp))

def print_character_attack(character, monster, is_crit):
    crit_text = MSG_CRITICAL_HIT if is_crit else ""
    print(MSG_CHARACTER_ATTACK.format(name=character.name, current_hp=character.current_hp, max_hp=character.max_hp, target=monster.name, crit=crit_text))

def team_attacks_monster(team, monster):
    for c in team:
        if not c.is_alive():
            continue

        is_crit = c.attack_target(monster)
        print_character_attack(c, monster, is_crit)

def get_cooldown_text(character):
    if character.is_ability_ready():
        return MSG_ABILITY_READY.format(ability=character.ability_name)
    return MSG_ABILITY_COOLDOWN.format(ability=character.ability_name, cooldown=character.current_cooldown)

def print_team_member_status(character):
    cooldown_text = get_cooldown_text(character)
    print(MSG_TEAM_MEMBER_STATUS.format(name=character.name, current_hp=character.current_hp, max_hp=character.max_hp, cooldown=cooldown_text))

def print_team_status(team):
    print(MSG_TEAM_STATUS)
    for c in team:
        if not c.is_alive():
            continue

        print_team_member_status(c)

def ask_ability_usage(character):
    if not character.is_ability_ready():
        return False

    response = input(MSG_ABILITY_PROMPT.format(name=character.name, ability=character.ability_name)).lower()
    return response == 'o'

def reduce_team_cooldowns(team):
    for c in team:
        if not c.is_alive():
            continue

        c.reduce_cooldown()

def handle_abilities(team, monster):
    for c in team:
        if c.is_alive() and ask_ability_usage(c):
            execute_ability(c, team, monster)
            if not monster.is_alive():
                return True
    return False

def check_monster_defeated(monster):
    if not monster.is_alive():
        print(MSG_MONSTER_DEFEATED)
        return True
    return False

def execute_player_turn(team, monster):
    if handle_abilities(team, monster):
        return check_monster_defeated(monster)

    team_attacks_monster(team, monster)
    return check_monster_defeated(monster)

def execute_monster_turn(monster, team):
    selected_c = monster_fight_character(monster, team)
    if not selected_c.is_alive():
        print(MSG_CHARACTER_DEFEATED.format(name=selected_c.name))

def combat_turn(team : list[Character], monster : Monster):
    print(MSG_COMBAT_TURN)
    print_monster_status(monster)

    if execute_player_turn(team, monster):
        reduce_team_cooldowns(team)
        print_team_status(team)
        return True

    execute_monster_turn(monster, team)
    reduce_team_cooldowns(team)
    print_team_status(team)
    return False

def select_random_target(team):
    return random.choice(team)

def print_monster_attack(monster, character, is_crit):
    crit_text = MSG_CRITICAL_HIT if is_crit else ""
    print(MSG_MONSTER_ATTACK.format(name=monster.name, target=character.name, current_hp=character.current_hp, max_hp=character.max_hp, crit=crit_text))

def monster_fight_character(monster : Monster, team : list[Character]):
    c = select_random_target(team)
    is_crit = monster.attack_target(c)
    print_monster_attack(monster, c, is_crit)
    return c

def is_team_alive(team):
    return any(char.is_alive() for char in team)

def fight_monster(team, monster):
    while monster.is_alive() and is_team_alive(team):
        if combat_turn(team, monster):
            break

    return is_team_alive(team)

def scale_monster_for_wave(monster, wave):
    hp_multiplier = 1 + (wave - 1) * WAVE_HP_MULTIPLIER
    stat_multiplier = 1 + (wave - 1) * WAVE_STAT_MULTIPLIER

    monster.max_hp = int(monster.max_hp * hp_multiplier)
    monster.current_hp = monster.max_hp
    monster.attack = int(monster.attack * stat_multiplier)
    monster.defense = int(monster.defense * stat_multiplier)

def apply_buffs_to_team(team):
    for c in team:
        if not c.is_alive():
            continue

        c.attack += TEAM_ATTACK_BUFF
        c.defense += TEAM_DEFENSE_BUFF
        c.max_hp += TEAM_HP_BUFF
        c.current_hp = min(c.max_hp, c.current_hp + TEAM_HP_BUFF)

def buff_team_after_wave(team, wave):
    print(MSG_WAVE_COMPLETE.format(wave=wave))
    apply_buffs_to_team(team)
    print(MSG_TEAM_BUFF)

def prepare_wave(db, wave):
    monster = get_random_monster(db)
    scale_monster_for_wave(monster, wave)
    print(MSG_WAVE_START.format(wave=wave, monster=monster.name))
    return monster

def start_combat(team : list[Character], db):
    wave = 0

    while is_team_alive(team):
        wave += 1
        monster = prepare_wave(db, wave)

        if not fight_monster(team, monster):
            break

        buff_team_after_wave(team, wave)

    return wave - 1 if wave > 0 else 0