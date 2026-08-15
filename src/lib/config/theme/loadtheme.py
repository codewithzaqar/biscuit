import json, os

class ThemeLoader:
    def __init__(self, master, theme_name="default"):
        self.base = master.base
        self.theme_name = theme_name
        self.theme_data = self.load_theme()

    def load_theme(self):
        path = os.path.join(self.base.appdir, 'config', 'themes', f'{self.theme_name}.json')
        try:
            with open(path, 'r') as themefile:
                return json.load(themefile)
        except FileNotFoundError:
            return {}

    def get_loaded_theme(self):
        return self.theme_data
