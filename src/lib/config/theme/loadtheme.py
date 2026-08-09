import json


class ThemeLoader:
    def __init__(self, theme_name, default="default"):
        self.theme_name = theme_name
        self.default = default
        self.try_load_theme()

    def try_load_theme(self):
        try:
            self.theme_data = self.load_theme()
        except Exception:
            self.theme_data = self.load_theme(self.default)

    def load_theme(self, name=None):
        name = name or self.theme_name
        with open(f'src/config/themes/{name}.json', 'r') as theme_file:
            return json.load(theme_file)

    def get_loaded_theme(self):
        return self.theme_data
