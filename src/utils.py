from models import Character, Monster

def create_character_from_db(char_data):
    # Character is initialized with both current hp and max hp at the same level, so we pass only hp.
    return Character(
        char_data['name'],
        char_data['attack'],
        char_data['defense'],
        char_data['hp']
    )

def create_monster_from_db(monster_data):
    # Same ^
    return Monster(
        monster_data['name'],
        monster_data['attack'],
        monster_data['defense'],
        monster_data['hp']
    )

def get_all_characters(db):
    characters_data = list(db.characters.find())
    return [create_character_from_db(c) for c in characters_data]

def get_all_monsters(db):
    monsters_data = list(db.monsters.find())
    return [create_monster_from_db(m) for m in monsters_data]

def get_random_monster(db):
    import random # Inline cuz imported from external file
    monster_data = random.choice(get_all_monsters(db))
    return monster_data

def save_score(db, username, score):
    db.leaderboard.insert_one({"username": username, "score": score})

def get_top_scores(db, limit=5):
    return list(db.leaderboard.find().sort("score", -1).limit(limit)) # -1 -> Descending order
