from db_init import init_database
from utils import get_all_characters, save_score, get_top_scores
from game import start_combat

def show_main_menu():
    print("")
    print("1. démarrer le jeu")
    print("2. afficher le classement")
    print("3. quitter")

def get_menu_choice():
    try:
        choice = input("\nChoix: ")
        return int(choice)

    except ValueError:
        return -1

def display_characters(characters):
    print("\nPersonnages disponibles:")

    for i, char in enumerate(characters, 1):
        stats = char.get_stats()
        print(f"{i}. {stats['name']} - {stats['attack']} d'attaque, {stats['defense']} de défense, {stats['max_hp']} points de vie")

def select_team(db):
    characters = get_all_characters(db)

    team = []
    while len(team) < 3:
        display_characters(characters)
        print(f"\nTeam: {[c.name for c in team]}")

        try:
            choice = int(input(f"Choisir personnage {len(team) + 1}: "))

            if 1 <= choice <= len(characters):
                selected = characters.pop(choice - 1)
                team.append(selected)
            else:
                raise ValueError

        except (ValueError, IndexError):
            print("Choix invalide")

    return team

def show_leaderboard(db):
    print("\nMeilleurs scores:")
    scores = get_top_scores(db)

    if len(scores) == 0:
        print("Aucun score dans la db")
    else:
        for i, entry in enumerate(scores, 1):
            print(f"{i}. {entry['username']} a survécu à {entry['score']} vagues")

def start_game(db):
    username = input("\nNom d'utilisateur: ") # TODO : Escape this
    team = select_team(db)

    print(f"\nTeam de {username}:")
    for char in team:
        print(f"- {char.name}")

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
                print("Babaye")
                break
            else:
                print("Choix invalide") # If -1 returned, that checks

    else:
        print("Pas de Db")

if __name__ == "__main__":
    main()