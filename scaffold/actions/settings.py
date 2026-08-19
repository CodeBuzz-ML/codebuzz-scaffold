from scaffold import ui
from scaffold.settings.manager import SettingsManager


def show_settings() -> None:
    settings = SettingsManager()

    while True:
        ui.header()
        ui.primary("Scaffold Settings")
        print()

        ui.option(1, f"Project location: {settings.project_location}")
        ui.option(2, f"Template: {settings.template}")
        ui.option(3, "Back")

        print()

        choice = input("Select an option: ").strip()

        if choice == "1":
            location = input("Enter project location: ")

            if settings.set_project_location(location):
                ui.accent("Project location updated.")
            else:
                ui.error("Project location cannot be empty.")

        elif choice == "2":
            template = input("Enter template: ")

            if settings.set_template(template):
                ui.accent("Template updated.")
            else:
                ui.error("Template cannot be empty.")

        elif choice == "3":
            break

        else:
            ui.error("Invalid option.")
