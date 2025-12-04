from models import Monster, Character
from utils import get_random_monster
from abilities import execute_ability
from messages import * # bunch of text
from config import * # bunch of numbers
import random

def print_monster_status(monster):
    print(MSG_MONSTER_STATUS.format(name=monster.name, current_hp=monster.current_hp, max_hp=monster.max_hp))

def team_attacks_monster(team, monster):
    for c in team:
        if c.is_alive():
            is_crit = c.attack_target(monster)
            crit_text = MSG_CRITICAL_HIT if is_crit else ""
            print(MSG_CHARACTER_ATTACK.format(name=c.name, current_hp=c.current_hp, max_hp=c.max_hp, target=monster.name, crit=crit_text))

def print_team_status(team):
    print(MSG_TEAM_STATUS)
    for c in team:
        if c.is_alive():
            cooldown_text = MSG_ABILITY_READY.format(ability=c.ability_name) if c.is_ability_ready() else MSG_ABILITY_COOLDOWN.format(ability=c.ability_name, cooldown=c.current_cooldown)
            print(MSG_TEAM_MEMBER_STATUS.format(name=c.name, current_hp=c.current_hp, max_hp=c.max_hp, cooldown=cooldown_text))

def ask_ability_usage(character):
    if not character.is_ability_ready():
        return False

    response = input(MSG_ABILITY_PROMPT.format(name=character.name, ability=character.ability_name)).lower()
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

def end_turn_cleanup(team):
    reduce_team_cooldowns(team)
    print_team_status(team)

def check_monster_defeated(monster):
    if not monster.is_alive():
        print(MSG_MONSTER_DEFEATED)
        return True
    return False

def combat_turn(team : list[Character], monster : Monster):
    print(MSG_COMBAT_TURN)
    print_monster_status(monster)

    if handle_abilities(team, monster) and check_monster_defeated(monster):
        end_turn_cleanup(team)
        return True

    team_attacks_monster(team, monster)

    if check_monster_defeated(monster):
        end_turn_cleanup(team)
        return True

    selected_c = monster_fight_character(monster, team)
    if not selected_c.is_alive():
        print(MSG_CHARACTER_DEFEATED.format(name=selected_c.name))

    end_turn_cleanup(team)
    return False

def monster_fight_character(monster : Monster, team : list[Character]):
    c = random.choice(team)
    is_crit = monster.attack_target(c)
    crit_text = MSG_CRITICAL_HIT if is_crit else ""
    print(MSG_MONSTER_ATTACK.format(name=monster.name, target=c.name, current_hp=c.current_hp, max_hp=c.max_hp, crit=crit_text))
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

def buff_team_after_wave(team, wave):
    print(MSG_WAVE_COMPLETE.format(wave=wave))
    for c in team:
        if c.is_alive():
            c.attack += TEAM_ATTACK_BUFF
            c.defense += TEAM_DEFENSE_BUFF
            c.max_hp += TEAM_HP_BUFF
            c.current_hp = min(c.max_hp, c.current_hp + TEAM_HP_BUFF)
    print(MSG_TEAM_BUFF)

def start_combat(team : list[Character], db):
    wave = 0

    while is_team_alive(team):
        wave += 1
        monster = get_random_monster(db)
        scale_monster_for_wave(monster, wave)
        print(MSG_WAVE_START.format(wave=wave, monster=monster.name))

        if not fight_monster(team, monster):
            break

        buff_team_after_wave(team, wave)

    return wave - 1 if wave > 0 else 0