from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Input field
        self.input_field = TextInput(hint_text="Enter some text", multiline=False, font_size=24)
        self.layout.add_widget(self.input_field)

        # Button
        show_btn = Button(text="Show Text", font_size=24)
        show_btn.bind(on_press=self.show_text)
        self.layout.add_widget(show_btn)

        # Label to display text
        self.output_label = Label(text="", font_size=28)
        self.layout.add_widget(self.output_label)

        return self.layout

    def show_text(self, instance):
        typed_text = self.input_field.text
        self.output_label.text = f"You typed: {typed_text}"

# Run the app
if __name__ == '__main__':
    TextInputApp().run()
