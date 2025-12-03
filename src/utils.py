from models import Character, Monster

def get_all_characters(db):
    characters_data = list(db.characters.find())
    return [Character.from_db(c) for c in characters_data]

def get_all_monsters(db):
    monsters_data = list(db.monsters.find())
    return [Monster.from_db(m) for m in monsters_data]

def get_random_monster(db):
    import random # Inline cuz imported from external file
    monster_data = random.choice(get_all_monsters(db))
    return monster_data

def save_score(db, username, score):
    db.leaderboard.insert_one({"username": username, "score": score})

def get_top_scores(db, limit=5):
    return list(db.leaderboard.find().sort("score", -1).limit(limit)) # -1 -> Descending order
