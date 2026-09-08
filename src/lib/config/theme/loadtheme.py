import json, os

class ThemeLoader:
    def __init__(self, master, theme_name):
        self.base = master.base
        self.theme_name = theme_name
        self.default = "light"  # Ensure you have a default theme JSON
        
        # Use try_load_theme to safely handle missing files
        self.theme_data = self.try_load_theme()

    def try_load_theme(self):
        try:
            return self.load_theme(self.theme_name)
        except Exception:
            self.base.trace(f"Theme '{self.theme_name}' not found, falling back to '{self.default}'")
            return self.load_theme(self.default)

    def load_theme(self, theme_name):
        # Using the path helper we added in Base
        with open(self.base.get_themes_path(f'{theme_name}.json'), 'r') as theme_file:
            theme_data = json.load(theme_file)
        return theme_data
