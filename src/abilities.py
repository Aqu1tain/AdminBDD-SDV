from messages import *

def cri_de_guerre(character, team, monster):
    for c in team:
        if c.is_alive():
            c.attack += 5
    print(MSG_ABILITY_CRI_GUERRE.format(name=character.name))

def boule_de_feu(character, team, monster):
    damage = character.attack * 2
    monster.take_damage(damage)
    print(MSG_ABILITY_BOULE_FEU.format(name=character.name, damage=int(damage)))

def tir_precis(character, team, monster):
    damage = character.attack * 3
    monster.take_damage(damage)
    print(MSG_ABILITY_TIR_PRECIS.format(name=character.name, damage=int(damage)))

def esquive(character, team, monster):
    character.defense += 20
    print(MSG_ABILITY_ESQUIVE.format(name=character.name))

def soin_divin(character, team, monster):
    lowest_hp_char = min((c for c in team if c.is_alive()), key=lambda c: c.current_hp)
    heal_amount = 30
    lowest_hp_char.current_hp = min(lowest_hp_char.max_hp, lowest_hp_char.current_hp + heal_amount)
    print(MSG_ABILITY_SOIN_DIVIN.format(name=character.name, target=lowest_hp_char.name, heal=heal_amount))

def eclair(character, team, monster):
    damage = character.attack * 2.5
    monster.take_damage(damage)
    print(MSG_ABILITY_ECLAIR.format(name=character.name, damage=int(damage)))

def bouclier(character, team, monster):
    for c in team:
        if c.is_alive():
            c.defense += 3
    print(MSG_ABILITY_BOUCLIER.format(name=character.name))

def meditation(character, team, monster):
    heal_amount = 25
    character.current_hp = min(character.max_hp, character.current_hp + heal_amount)
    print(MSG_ABILITY_MEDITATION.format(name=character.name, heal=heal_amount))

def rage(character, team, monster):
    damage = character.attack * 4
    self_damage = 15
    monster.take_damage(damage)
    character.current_hp = max(0, character.current_hp - self_damage)
    print(MSG_ABILITY_RAGE.format(name=character.name, damage=int(damage), self_damage=self_damage))

def piege(character, team, monster):
    damage = character.attack * 2
    monster.take_damage(damage)
    print(MSG_ABILITY_PIEGE.format(name=character.name, damage=int(damage)))

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
