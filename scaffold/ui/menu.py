from scaffold import __version__, ui
from scaffold.ui.colors import ACCENT, ERROR, HIGHLIGHT, RESET

ui.header(50)  # Display the header with a width of 50


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
        ui.accent("Create a new project selected.")
    elif choice == 2:
        ui.accent("Browse templates selected.")
    elif choice == 3:
        ui.accent("Settings selected.")
    elif choice == 4:
        show_about()
    elif choice == 5:
        ui.exit_app()
        return False

    return True


def show_about() -> None:
    ui.header()

    ui.primary("About CodeBuzz Scaffold")
    print()

    print("CodeBuzz Scaffold is a project scaffolding")
    print("tool designed to make creating new projects")
    print("quick, consistent, and easy.")

    print()
    ui.accent(f"Version: {__version__}")
    ui.accent("Author: Advait Muley")

    print()
    ui.muted("Press Enter to return to the main menu...")
    input()
