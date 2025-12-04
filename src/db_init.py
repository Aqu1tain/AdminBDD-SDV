from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from constants import *

def connect_to_db():
    try:
        client = MongoClient(f"mongodb://{DB_HOST}:{DB_PORT}/")
        client.admin.command("ping")
        db = client[DB_NAME]

        print(MSG_DB_CONNECT_SUCCESS)
        return db

    except ConnectionFailure:
        print(MSG_DB_CONNECT_FAIL)
        return None

def get_characters_data():
    return [
        {"name": "Guerrier", "attack": 15, "defense": 10, "hp": 100, "critical_chance": 20, "ability_name": "Cri de guerre", "ability_cooldown": 3},
        {"name": "Mage", "attack": 20, "defense": 5, "hp": 80, "critical_chance": 10, "ability_name": "Boule de feu", "ability_cooldown": 4},
        {"name": "Archer", "attack": 18, "defense": 7, "hp": 90, "critical_chance": 25, "ability_name": "Tir precis", "ability_cooldown": 3},
        {"name": "Voleur", "attack": 22, "defense": 8, "hp": 85, "critical_chance": 30, "ability_name": "Esquive", "ability_cooldown": 4},
        {"name": "Paladin", "attack": 14, "defense": 12, "hp": 110, "critical_chance": 15, "ability_name": "Soin divin", "ability_cooldown": 5},
        {"name": "Sorcier", "attack": 25, "defense": 3, "hp": 70, "critical_chance": 12, "ability_name": "Eclair", "ability_cooldown": 3},
        {"name": "Chevalier", "attack": 17, "defense": 15, "hp": 120, "critical_chance": 18, "ability_name": "Bouclier", "ability_cooldown": 4},
        {"name": "Moine", "attack": 19, "defense": 9, "hp": 95, "critical_chance": 22, "ability_name": "Meditation", "ability_cooldown": 4},
        {"name": "Berserker", "attack": 23, "defense": 6, "hp": 105, "critical_chance": 35, "ability_name": "Rage", "ability_cooldown": 3},
        {"name": "Chasseur", "attack": 16, "defense": 11, "hp": 100, "critical_chance": 28, "ability_name": "Piege", "ability_cooldown": 4},
    ]

def get_monsters_data():
    return [
        {"name": "Gobelin", "attack": 10, "defense": 5, "hp": 50},
        {"name": "Orc", "attack": 20, "defense": 8, "hp": 120},
        {"name": "Dragon", "attack": 35, "defense": 20, "hp": 300},
        {"name": "Zombie", "attack": 12, "defense": 6, "hp": 70},
        {"name": "Troll", "attack": 25, "defense": 15, "hp": 200},
        {"name": "Spectre", "attack": 18, "defense": 10, "hp": 100},
        {"name": "Golem", "attack": 30, "defense": 25, "hp": 250},
        {"name": "Vampire", "attack": 22, "defense": 12, "hp": 150},
        {"name": "Loup-garou", "attack": 28, "defense": 18, "hp": 180},
        {"name": "Squelette", "attack": 15, "defense": 7, "hp": 90},
    ]

def insert_characters(db):
    try:
        db.characters.drop()
        characters = get_characters_data()
        db.characters.insert_many(characters)
        print(MSG_DB_CHARS_INSERTED.format(count=len(characters)))

    except OperationFailure as e:
        raise Exception(f"Failed to insert characters: {e}")

def insert_monsters(db):
    try:
        db.monsters.drop()
        monsters = get_monsters_data()
        db.monsters.insert_many(monsters)
        print(MSG_DB_MONSTERS_INSERTED.format(count=len(monsters)))

    except OperationFailure as e:
        raise Exception(f"Failed to insert monsters: {e}")

def init_leaderboard(db):
    try:
        if "leaderboard" not in db.list_collection_names():
            db.create_collection("leaderboard")
            print(MSG_DB_LEADERBOARD_INIT)
        else:
            print(MSG_DB_LEADERBOARD_EXISTS)
    except OperationFailure as e:
        raise Exception(f"Failed to initialize leaderboard: {e}")

def init_database():
    db = connect_to_db()

    if db is None:
        return False

    try:
        insert_characters(db)
        insert_monsters(db)
        init_leaderboard(db)
        return db

    except Exception as e:
        print(e)
        return False