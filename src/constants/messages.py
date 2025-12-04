# combat messages
MSG_COMBAT_TURN = "\nTour de combat"
MSG_MONSTER_STATUS = "Monstre: {name} ({current_hp}/{max_hp} points de vie)"
MSG_CHARACTER_ATTACK = "{name} : {current_hp}/{max_hp} attaque {target}{crit}"
MSG_MONSTER_ATTACK = "Monstre : {name} attaque {target} ({current_hp}/{max_hp} points de vie){crit}"
MSG_CRITICAL_HIT = " COUP CRITIQUE!"
MSG_MONSTER_DEFEATED = "Le monstre a ete vaincu"
MSG_CHARACTER_DEFEATED = "{name} a ete vaincu"
MSG_TEAM_STATUS = "\nÉtat de l'équipe:"
MSG_TEAM_MEMBER_STATUS = "  {name}: {current_hp}/{max_hp} HP{cooldown}"
MSG_ABILITY_READY = " [{ability}: pret]"
MSG_ABILITY_COOLDOWN = " [{ability}: {cooldown} tours]"

# abilitess messages
MSG_ABILITY_CRI_GUERRE = "{name} utilise Cri de guerre! Attaque de l'equipe +5"
MSG_ABILITY_BOULE_FEU = "{name} lance Boule de feu! {damage} degats au monstre"
MSG_ABILITY_TIR_PRECIS = "{name} utilise Tir precis! COUP GARANTI: {damage} degats"
MSG_ABILITY_ESQUIVE = "{name} utilise Esquive! Defense +20 pour ce tour"
MSG_ABILITY_SOIN_DIVIN = "{name} utilise Soin divin! {target} recupere {heal} HP"
MSG_ABILITY_ECLAIR = "{name} lance Eclair! {damage} degats de foudre"
MSG_ABILITY_BOUCLIER = "{name} utilise Bouclier! Defense de l'equipe +3"
MSG_ABILITY_MEDITATION = "{name} utilise Meditation et recupere {heal} HP"
MSG_ABILITY_RAGE = "{name} utilise Rage! {damage} degats mais perd {self_damage} HP"
MSG_ABILITY_PIEGE = "{name} pose un Piege! {damage} degats au monstre"
MSG_ABILITY_PROMPT = "{name} peut utiliser {ability}. Utiliser? (o/n): "

# wave related messages
MSG_WAVE_START = "\nVague {wave} - {monster} apparait!"
MSG_WAVE_COMPLETE = "\nVague {wave} terminee! L'equipe devient plus forte!"
MSG_TEAM_BUFF = "Equipe: +3 attaque, +2 defense, +5 HP max"

# menu related messages
MSG_MENU_EMPTY_LINE = ""
MSG_MENU_START_GAME = "1. démarrer le jeu"
MSG_MENU_LEADERBOARD = "2. afficher le classement"
MSG_MENU_QUIT = "3. quitter"
MSG_MENU_CHOICE_PROMPT = "\nChoix: "
MSG_MENU_INVALID_CHOICE = "Choix invalide"
MSG_MENU_GOODBYE = "Babaye"

# character selection related messages
MSG_CHAR_AVAILABLE = "\nPersonnages disponibles:"
MSG_CHAR_STATS = "{num}. {name} - {attack} d'attaque, {defense} de défense, {hp} points de vie"
MSG_TEAM_CURRENT = "\nTeam: {team}"
MSG_TEAM_CHOICE_PROMPT = "Choisir personnage {num}: "
MSG_USERNAME_PROMPT = "\nNom d'utilisateur: "
MSG_TEAM_FINAL = "\nTeam de {username}:"
MSG_TEAM_MEMBER = "- {name}"

# leaderboard related messages
MSG_LEADERBOARD_TITLE = "\nMeilleurs scores:"
MSG_LEADERBOARD_EMPTY = "Aucun score dans la db"
MSG_LEADERBOARD_ENTRY = "{rank}. {username} a survécu à {score} vagues"

# db related messages
MSG_DB_CONNECT_SUCCESS = "Connected to MongoDB"
MSG_DB_CONNECT_FAIL = "Failed to connect to MongoDB."
MSG_DB_CHARS_INSERTED = "Inserted {count} characters"
MSG_DB_MONSTERS_INSERTED = "Inserted {count} monsters"
MSG_DB_LEADERBOARD_INIT = "Initialized leaderboard"
MSG_DB_LEADERBOARD_EXISTS = "Leaderboard already exists"
MSG_DB_NO_CONNECTION = "No database was found"
