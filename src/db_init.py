from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure


def connect_to_db():
    try:
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
        db = client["game_db"]
        print("✓ Connected to MongoDB")
        return db
    except ConnectionFailure:
        print("✗ Failed to connect to MongoDB. Is it running?")
        return None


def get_characters_data():
    return [
        {"name": "Guerrier", "attack": 15, "defense": 10, "hp": 100},
        {"name": "Mage", "attack": 20, "defense": 5, "hp": 80},
        {"name": "Archer", "attack": 18, "defense": 7, "hp": 90},
        {"name": "Voleur", "attack": 22, "defense": 8, "hp": 85},
        {"name": "Paladin", "attack": 14, "defense": 12, "hp": 110},
        {"name": "Sorcier", "attack": 25, "defense": 3, "hp": 70},
        {"name": "Chevalier", "attack": 17, "defense": 15, "hp": 120},
        {"name": "Moine", "attack": 19, "defense": 9, "hp": 95},
        {"name": "Berserker", "attack": 23, "defense": 6, "hp": 105},
        {"name": "Chasseur", "attack": 16, "defense": 11, "hp": 100},
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
        print(f"✓ Inserted {len(characters)} characters")
    except OperationFailure as e:
        raise Exception(f"Failed to insert characters: {e}")


def insert_monsters(db):
    try:
        db.monsters.drop()
        monsters = get_monsters_data()
        db.monsters.insert_many(monsters)
        print(f"✓ Inserted {len(monsters)} monsters")
    except OperationFailure as e:
        raise Exception(f"Failed to insert monsters: {e}")


def init_leaderboard(db):
    try:
        db.leaderboard.drop()
        db.create_collection("leaderboard")
        print("✓ Initialized leaderboard")
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
        return True
    except Exception as e:
        print(f"✗ {e}")
        return False


if __name__ == "__main__":
    print("Initializing game database...")
    if init_database():
        print("\n✓ Database initialization complete!")
    else:
        print("\n✗ Database initialization failed")
