from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.counter = 0  # Initialize counter

        # Main vertical layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Label to display count
        self.label = Label(text="Counter: 0", font_size=32)
        layout.add_widget(self.label)

        # Button to increment counter
        increment_btn = Button(text="Increment", font_size=24)
        increment_btn.bind(on_press=self.increment_counter)
        layout.add_widget(increment_btn)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"Counter: {self.counter}"

# Run the app
if __name__ == '__main__':
    CounterApp().run()
