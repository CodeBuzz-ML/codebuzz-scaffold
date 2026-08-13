from scaffold.ui.colors import ACCENT, BOLD, ERROR, HIGHLIGHT, PRIMARY, RESET


def show_header() -> None:
    width = 44

    print()
    print(f"{PRIMARY}{BOLD}╭{'─' * width}╮")
    print(f"{PRIMARY}{BOLD}│{'CODEBUZZ SCAFFOLD':^{width}}│")
    print(f"{PRIMARY}{BOLD}│{'Project creation made easy':^{width}}│")
    print(f"{PRIMARY}{BOLD}╰{'─' * width}╯")
    print()


def show_menu() -> None:
    print(f"{HIGHLIGHT}{BOLD}What would you like to do?{RESET}")
    print()

    print(f"{ACCENT}[1]{RESET}  Create a new project")
    print(f"{ACCENT}[2]{RESET}  Browse templates")
    print(f"{ACCENT}[3]{RESET}  Settings")
    print(f"{ACCENT}[4]{RESET}  About")
    print(f"{ACCENT}[5]{RESET}  Exit")

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
