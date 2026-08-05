import argparse
from scaffold import __version__

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='scaffold',
        description="CodeBuzz Scaffold - A modern project scaffolding CLI.",
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    create_parser = subparsers.add_parser(
        "create",
        help="Create a new project."
    )   
    create_parser.add_argument(
        "name",
        help="Project name."
    )
    return parser