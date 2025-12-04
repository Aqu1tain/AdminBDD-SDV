def cri_de_guerre(character, team, monster):
    for c in team:
        if c.is_alive():
            c.attack += 5
    print(f"{character.name} utilise Cri de guerre! Attaque de l'equipe +5")

def boule_de_feu(character, team, monster):
    damage = character.attack * 2
    monster.take_damage(damage)
    print(f"{character.name} lance Boule de feu! {int(damage)} degats au monstre")

def tir_precis(character, team, monster):
    damage = character.attack * 3
    monster.take_damage(damage)
    print(f"{character.name} utilise Tir precis! COUP GARANTI: {int(damage)} degats")

def esquive(character, team, monster):
    character.defense += 20
    print(f"{character.name} utilise Esquive! Defense +20 pour ce tour")

def soin_divin(character, team, monster):
    lowest_hp_char = min((c for c in team if c.is_alive()), key=lambda c: c.current_hp)
    heal_amount = 30
    lowest_hp_char.current_hp = min(lowest_hp_char.max_hp, lowest_hp_char.current_hp + heal_amount)
    print(f"{character.name} utilise Soin divin! {lowest_hp_char.name} recupere {heal_amount} HP")

def eclair(character, team, monster):
    damage = character.attack * 2.5
    monster.take_damage(damage)
    print(f"{character.name} lance Eclair! {int(damage)} degats de foudre")

def bouclier(character, team, monster):
    for c in team:
        if c.is_alive():
            c.defense += 3
    print(f"{character.name} utilise Bouclier! Defense de l'equipe +3")

def meditation(character, team, monster):
    heal_amount = 25
    character.current_hp = min(character.max_hp, character.current_hp + heal_amount)
    print(f"{character.name} utilise Meditation et recupere {heal_amount} HP")

def rage(character, team, monster):
    damage = character.attack * 4
    self_damage = 15
    monster.take_damage(damage)
    character.current_hp = max(0, character.current_hp - self_damage)
    print(f"{character.name} utilise Rage! {int(damage)} degats mais perd {self_damage} HP")

def piege(character, team, monster):
    damage = character.attack * 2
    monster.take_damage(damage)
    print(f"{character.name} pose un Piege! {int(damage)} degats au monstre")

ABILITIES = {
    "Cri de guerre": cri_de_guerre,
    "Boule de feu": boule_de_feu,
    "Tir precis": tir_precis,
    "Esquive": esquive,
    "Soin divin": soin_divin,
    "Eclair": eclair,
    "Bouclier": bouclier,
    "Meditation": meditation,
    "Rage": rage,
    "Piege": piege,
}

def execute_ability(character, team, monster):
    ability_func = ABILITIES.get(character.ability_name)
    if ability_func:
        ability_func(character, team, monster)
        character.use_ability_cooldown()
