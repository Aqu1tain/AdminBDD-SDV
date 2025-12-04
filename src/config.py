# Config file for the game
# Feel free to change the values to match your ideal vision of what fun is.
# Anyways, if you fun is to move around some values, you *should* question yourself XD

# team
TEAM_SIZE = 3

# wave diff scaling
WAVE_HP_MULTIPLIER = 0.15  # +15% HP per wave
WAVE_STAT_MULTIPLIER = 0.10  # +10% attack/defense per wave

# team progression (per wave survived)
TEAM_ATTACK_BUFF = 3
TEAM_DEFENSE_BUFF = 2
TEAM_HP_BUFF = 5

# combat
DEFENSE_DAMAGE_REDUCTION = 2  # damages reduced by defense / DEFENSE_DAMAGE_REDUCTION

# abilities stuff
ABILITY_BOULE_FEU_MULTIPLIER = 2.0
ABILITY_TIR_PRECIS_MULTIPLIER = 3.0
ABILITY_ECLAIR_MULTIPLIER = 2.5
ABILITY_RAGE_MULTIPLIER = 4.0
ABILITY_PIEGE_MULTIPLIER = 2.0

ABILITY_CRI_GUERRE_BUFF = 5
ABILITY_ESQUIVE_BUFF = 20
ABILITY_BOUCLIER_BUFF = 3

ABILITY_SOIN_DIVIN_HEAL = 30
ABILITY_MEDITATION_HEAL = 25

ABILITY_RAGE_SELF_DAMAGE = 15

# db config
DB_HOST = "localhost"
DB_PORT = 27017
DB_NAME = "game_db"
DB_COLLECTION_CHARACTERS = "characters"
DB_COLLECTION_MONSTERS = "monsters"
DB_COLLECTION_LEADERBOARD = "leaderboard"

# leaderboard
LEADERBOARD_DEFAULT_LIMIT = 5
