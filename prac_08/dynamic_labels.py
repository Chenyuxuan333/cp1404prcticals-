"""
CP1404 Practical 08
Dynamic labels
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


class DynamicLabelsApp(App):
    """App that creates Labels dynamically from a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

    def build(self):
        """Load the KV layout and add labels dynamically."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()

        total_height = 40 * len(self.names) + 5 * (len(self.names) - 1)
        Window.size = (400, total_height)

        return self.root

    def create_labels(self):
        """Create Label widgets from name list."""
        for i, name in enumerate(self.names):
            label_box = BoxLayout(size_hint_y=None, height=40, padding=5)

            # Alternating background color
            with label_box.canvas.before:
                if i % 2 == 0:
                    Color(0, 0, 0, 1)  # black
                else:
                    Color(0.5, 0.5, 0.5, 1)  # grey
                label_box.rect = Rectangle(pos=label_box.pos, size=label_box.size)

            label_box.bind(pos=self.update_rectangle, size=self.update_rectangle)

            label = Label(text=name, color=(1, 1, 1, 1))  # white text
            label_box.add_widget(label)
            self.root.ids.entries_box.add_widget(label_box)

    def update_rectangle(self, instance, _):
        """Ensure background rectangle follows widget resizing."""
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

if __name__ == '__main__':
    DynamicLabelsApp().run()