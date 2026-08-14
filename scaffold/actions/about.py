from scaffold import __version__, ui


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
