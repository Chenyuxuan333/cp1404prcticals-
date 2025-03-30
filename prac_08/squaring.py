"""
CP1404 Practical 08
Kivy GUI program to square a number

Started 26/03/2025
"""

# from Demos.win32console_demo import window_size
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Minzhi Liu'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 100)    # Set the initial window size
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)

            # Resize the window to fit the label
            label = self.root.ids.output_label
            label_width = label.texture_size[0] + 40
            Window.size = (max(300, label_width), 100)
        except ValueError:
            pass


SquareNumberApp().run()