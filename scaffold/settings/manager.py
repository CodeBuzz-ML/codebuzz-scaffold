from scaffold.settings import defaults


class SettingsManager:
    def __init__(self) -> None:
        self.project_location = defaults.DEFAULT_PROJECT_LOCATION
        self.template = defaults.DEFAULT_TEMPLATE

    def set_project_location(self, location: str) -> bool:
        location = location.strip()

        if not location:
            return False

        self.project_location = location
        return True

    def set_template(self, template: str) -> bool:
        template = template.strip()

        if not template:
            return False

        self.template = template
        return True
