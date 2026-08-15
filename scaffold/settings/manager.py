from scaffold.settings import defaults

class SettingsManager:
    def __init__(self) -> None:
        self.project_location = defaults.DEFAULT_PROJECT_LOCATION
        self.template = defaults.DEFAULT_TEMPLATE