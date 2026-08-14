import argparse

from scaffold import __version__, ui
from scaffold.ui.menu import get_menu_choice, handle_menu_choice, show_menu


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scaffold",
        description="CodeBuzz Scaffold - A modern project scaffolding CLI.",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def run_interactive() -> None:

    while True:
        ui.header(50)
        show_menu()
        choice = get_menu_choice()

        if not handle_menu_choice(choice):
            break


def main() -> None:
    parser = build_parser()
    parser.parse_args()

    run_interactive()
