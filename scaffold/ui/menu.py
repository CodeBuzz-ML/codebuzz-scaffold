from scaffold import ui
from scaffold.actions import about
from scaffold.ui.colors import ACCENT, ERROR, HIGHLIGHT, RESET

ui.clear()


def show_menu() -> None:
    ui.primary("What would you like to do?")
    print()

    ui.option(1, "Create a new project")
    ui.option(2, "Browse templates")
    ui.option(3, "Settings")
    ui.option(4, "About")
    ui.option(5, "Exit")

    print()


def get_menu_choice() -> int:
    while True:
        try:
            choice = int(input(f"{ACCENT}Select an option [1-5]: {RESET}").strip())

            if 1 <= choice <= 5:
                return choice
            else:
                print(f"{ERROR}Please enter a number between 1 and 5.")
        except ValueError:
            print(f"{ERROR}Invalid input. Please enter a number between 1 and 5.")
        except KeyboardInterrupt:
            print()
            print(f"{HIGHLIGHT}Exiting CodeBuzz Scaffold{RESET}")
            raise SystemExit


def handle_menu_choice(choice: int) -> bool:
    if choice == 1:
        ui.clear()
        ui.accent("Create a new project selected.")
    elif choice == 2:
        ui.clear()
        ui.accent("Browse templates selected.")
    elif choice == 3:
        ui.clear()
        ui.accent("Settings selected.")
    elif choice == 4:
        ui.clear()
        about.show_about()
    elif choice == 5:
        ui.clear()
        ui.exit_app()
        return False

    return True
