from scaffold import ui
from scaffold.settings.manager import SettingsManager


def show_settings() -> None:
    settings = SettingsManager()

    ui.header()
    ui.primary("Scaffold Settings")
    print()

    ui.option(1, f"Project location: {settings.project_location}")
    ui.option(2, f"Template: {settings.template}")
    ui.option(3, "Back")

    print()