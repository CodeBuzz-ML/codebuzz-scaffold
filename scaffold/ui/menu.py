from scaffold.ui.colors import (
    ACCENT,
    BOLD,
    HIGHLIGHT,
    PRIMARY,
    RESET,
)


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
