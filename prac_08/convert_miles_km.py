"""
CP1404 Practical 08
Convert miles to kilometers
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    output_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.output_text = "0.0"
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, text):
        """Convert miles to km."""
        try:
            miles = float(text)
        except ValueError:
            miles = 0.0
        km = miles * MILE_TO_KM
        self.output_text = str(km)

    def handle_increment(self, text, change):
        """Increase/decrease miles by 1 and convert."""
        try:
            miles = int(text)
        except ValueError:
            miles = 0
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_conversion(str(miles))

    def convert_to_number(self, text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


if __name__ == '__main__':
    ConvertMilesKmApp().run()