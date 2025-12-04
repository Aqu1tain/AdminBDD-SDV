from db_init import init_database
from utils import get_all_characters, save_score, get_top_scores
from game import start_combat
from constants import *

def show_main_menu():
    print(MSG_MENU_EMPTY_LINE)
    print(MSG_MENU_START_GAME)
    print(MSG_MENU_LEADERBOARD)
    print(MSG_MENU_QUIT)

def get_menu_choice():
    try:
        choice = input(MSG_MENU_CHOICE_PROMPT)
        return int(choice)

    except ValueError:
        return -1

def display_characters(characters):
    print(MSG_CHAR_AVAILABLE)

    for i, char in enumerate(characters, 1):
        stats = char.get_stats()
        print(MSG_CHAR_STATS.format(num=i, name=stats['name'], attack=stats['attack'], defense=stats['defense'], hp=stats['max_hp']))

def select_team(db):
    characters = get_all_characters(db)

    team = []
    while len(team) < TEAM_SIZE:
        display_characters(characters)
        print(MSG_TEAM_CURRENT.format(team=[c.name for c in team]))

        try:
            choice = int(input(MSG_TEAM_CHOICE_PROMPT.format(num=len(team) + 1)))

            if 1 <= choice <= len(characters):
                selected = characters.pop(choice - 1)
                team.append(selected)
            else:
                raise ValueError

        except (ValueError, IndexError):
            print(MSG_MENU_INVALID_CHOICE)

    return team

def show_leaderboard(db):
    print(MSG_LEADERBOARD_TITLE)
    scores = get_top_scores(db)

    if len(scores) == 0:
        print(MSG_LEADERBOARD_EMPTY)
    else:
        for i, entry in enumerate(scores, 1):
            print(MSG_LEADERBOARD_ENTRY.format(rank=i, username=entry['username'], score=entry['score']))

def start_game(db):
    username = input(MSG_USERNAME_PROMPT)
    team = select_team(db)

    print(MSG_TEAM_FINAL.format(username=username))
    for char in team:
        print(MSG_TEAM_MEMBER.format(name=char.name))

    score = start_combat(team, db)
    save_score(db, username, score)

def main():
    db = init_database()

    if db is not False :
        while True:
            show_main_menu()
            choice = get_menu_choice()

            if choice == 1:
                start_game(db)
            elif choice == 2:
                show_leaderboard(db)
            elif choice == 3:
                print(MSG_MENU_GOODBYE)
                break
            else:
                print(MSG_MENU_INVALID_CHOICE)

    else:
        print(MSG_DB_NO_CONNECTION)

if __name__ == "__main__":
    main()