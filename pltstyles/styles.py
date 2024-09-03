import os
import matplotlib.pyplot as plt


class Styles:
    def __init__(self, plt_obj):
        path = os.path.dirname(__file__)
        # go one level above
        path = os.path.dirname(path)
        self.styles_path = os.path.join(path, 'styles')
        self.plt_obj = plt_obj

    def get_styles(self):
        return os.listdir(self.styles_path)

    def apply_style(self, style):
        # check if style has a suffix
        if not style.endswith('.mplstyle'):
            style = style + '.mplstyle'
        available_styles = self.get_styles()
        if style in available_styles:
            self.plt_obj.style.use(os.path.join(self.styles_path, style))
        else:
            print(
                f"Style '{style}' not found. Available styles: {', '.join(available_styles)}")
