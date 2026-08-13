from colorama import Fore, Style, init

init(autoreset=True)


# CodeBuzz brand colours
PRIMARY = Fore.MAGENTA
SECONDARY = Fore.BLUE
ACCENT = Fore.CYAN
HIGHLIGHT = Fore.LIGHTMAGENTA_EX

TEXT = Fore.WHITE
MUTED = Fore.LIGHTBLACK_EX

SUCCESS = Fore.GREEN
WARNING = Fore.YELLOW
ERROR = Fore.RED

BOLD = Style.BRIGHT
DIM = Style.DIM
RESET = Style.RESET_ALL

#Add print functions for colors
def print_accent(text: str) -> None:
    print(f"{ACCENT}{text}{RESET}")


def print_success(text: str) -> None:
    print(f"{SUCCESS}{text}{RESET}")


def print_warning(text: str) -> None:
    print(f"{WARNING}{text}{RESET}")


def print_error(text: str) -> None:
    print(f"{ERROR}{text}{RESET}")


def print_primary(text: str) -> None:
    print(f"{PRIMARY}{text}{RESET}")