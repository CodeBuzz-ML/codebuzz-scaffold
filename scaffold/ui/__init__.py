from scaffold.ui.colors import (
    ACCENT,
    BOLD,
    ERROR,
    HIGHLIGHT,
    MUTED,
    PRIMARY,
    RESET,
    SUCCESS,
    TEXT,
    WARNING,
)


# Define functions for printing
def accent(text: str) -> None:
    print(f"{ACCENT}{text}{RESET}")


def success(text: str) -> None:
    print(f"{SUCCESS}{text}{RESET}")


def warning(text: str) -> None:
    print(f"{WARNING}{text}{RESET}")


def error(text: str) -> None:
    print(f"{ERROR}{text}{RESET}")


def primary(text: str) -> None:
    print(f"{PRIMARY}{text}{RESET}")


def highlight(text: str) -> None:
    print(f"{HIGHLIGHT}{text}{RESET}")


def text(text: str) -> None:
    print(f"{TEXT}{text}{RESET}")


def option(number: int, text: str) -> None:
    print(f"{ACCENT}[{number}]{RESET}  {text}")


def muted(text: str) -> None:
    print(f"{MUTED}{text}{RESET}")


# Define function for header block


def header(width: int = 44) -> None:
    print()
    print(f"{PRIMARY}{BOLD}╭{'─' * width}╮")
    print(f"{PRIMARY}{BOLD}│{'CODEBUZZ SCAFFOLD':^{width}}│")
    print(f"{PRIMARY}{BOLD}│{'Project creation made easy':^{width}}│")
    print(f"{PRIMARY}{BOLD}╰{'─' * width}╯")
    print()


def exit_app() -> None:
    print()
    accent("Exiting CodeBuzz Scaffold...")
    print()
