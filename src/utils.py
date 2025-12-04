from models import Character, Monster
from constants import *
import random

def get_all_characters(db):
    characters_data = list(db.characters.find())
    return [Character.from_db(c) for c in characters_data]

def get_all_monsters(db):
    monsters_data = list(db.monsters.find())
    return [Monster.from_db(m) for m in monsters_data]

def get_random_monster(db):
    monster_data = random.choice(get_all_monsters(db))
    return monster_data

def save_score(db, username, score):
    db.leaderboard.insert_one({"username": username, "score": score})

def get_top_scores(db, limit=LEADERBOARD_DEFAULT_LIMIT):
    return list(db.leaderboard.find().sort("score", -1).limit(limit))

def select_random_target(team):
    alive_members = [char for char in team if char.is_alive()]
    return random.choice(alive_members)

def is_team_alive(team):
    return any(char.is_alive() for char in team)

def get_cooldown_text(character):
    if character.is_ability_ready():
        return MSG_ABILITY_READY.format(ability=character.ability_name)
    return MSG_ABILITY_COOLDOWN.format(ability=character.ability_name, cooldown=character.current_cooldown)

def get_crit_text(is_crit):
    return MSG_CRITICAL_HIT if is_crit else ""

def get_int_input(prompt, default_on_error=None):
    try:
        return int(input(prompt))
    except ValueError:
        return default_on_error

def for_each_alive_member(team, action):
    for member in team:
        if not member.is_alive():
            continue

        action(member)
