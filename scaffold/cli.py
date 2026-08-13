import argparse

from scaffold import __version__
from scaffold.ui.menu import get_menu_choice, show_header, show_menu


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
    show_header()
    show_menu()
    get_menu_choice()


def main() -> None:
    parser = build_parser()
    parser.parse_args()

    run_interactive()
