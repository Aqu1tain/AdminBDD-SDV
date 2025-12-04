from db_init import init_database
from utils import get_all_characters, save_score, get_top_scores
from game import start_combat
from constants import *

def show_main_menu():
    print(MSG_MENU_START_GAME)
    print(MSG_MENU_LEADERBOARD)
    print(MSG_MENU_QUIT)

def get_menu_choice():
    try:
        choice = input(MSG_MENU_CHOICE_PROMPT)
        return int(choice)

    except ValueError:
        return -1

def print_character_info(index, character):
    stats = character.get_stats()
    print(MSG_CHAR_STATS.format(num=index, name=stats['name'], attack=stats['attack'], defense=stats['defense'], hp=stats['max_hp']))

def display_characters(characters):
    print(MSG_CHAR_AVAILABLE)
    for i, char in enumerate(characters, 1):
        print_character_info(i, char)

def get_character_choice_input(position):
    try:
        choice = int(input(MSG_TEAM_CHOICE_PROMPT.format(num=position)))
        return choice
    except ValueError:
        return None

def try_add_character_to_team(characters, team, choice):
    if choice is None or choice < 1 or choice > len(characters):
        print(MSG_MENU_INVALID_CHOICE)
        return False

    selected = characters.pop(choice - 1)
    team.append(selected)
    return True

def select_team(db):
    characters = get_all_characters(db)
    team = []

    while len(team) < TEAM_SIZE:
        display_characters(characters)
        print(MSG_TEAM_CURRENT.format(team=[c.name for c in team]))

        choice = get_character_choice_input(len(team) + 1)
        try_add_character_to_team(characters, team, choice)

    return team

def print_leaderboard_entries(scores):
    if len(scores) == 0:
        print(MSG_LEADERBOARD_EMPTY)
    else:
        for i, entry in enumerate(scores, 1):
            print(MSG_LEADERBOARD_ENTRY.format(rank=i, username=entry['username'], score=entry['score']))

def show_leaderboard(db):
    print(MSG_LEADERBOARD_TITLE)
    scores = get_top_scores(db)
    print_leaderboard_entries(scores)

def print_selected_team(username, team):
    print(MSG_TEAM_FINAL.format(username=username))
    for char in team:
        print(MSG_TEAM_MEMBER.format(name=char.name))

def start_game(db):
    username = input(MSG_USERNAME_PROMPT)
    team = select_team(db)

    print_selected_team(username, team)

    score = start_combat(team, db)
    save_score(db, username, score)

def handle_menu_choice(db, choice):
    if choice == 1:
        start_game(db)
    elif choice == 2:
        show_leaderboard(db)
    elif choice == 3:
        print(MSG_MENU_GOODBYE)
        return False
    else:
        print(MSG_MENU_INVALID_CHOICE)
    return True

def run_game_loop(db):
    while True:
        show_main_menu()
        choice = get_menu_choice()

        if not handle_menu_choice(db, choice):
            break

def main():
    db = init_database()

    if db is False:
        print(MSG_DB_NO_CONNECTION)
        return

    run_game_loop(db)

if __name__ == "__main__":
    main()