from scaffold.settings import defaults


class SettingsManager:
    def __init__(self) -> None:
        self.project_location = defaults.DEFAULT_PROJECT_LOCATION
        self.template = defaults.DEFAULT_TEMPLATE

    def set_project_location(self, location: str) -> None:
        self.project_location = location

    def set_template(self, template: str) -> None:
        self.template = template
