from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.num1 = TextInput(
            hint_text="पहिली संख्या",
            multiline=False,
            input_filter="float"
        )

        self.num2 = TextInput(
            hint_text="दुसरी संख्या",
            multiline=False,
            input_filter="float"
        )

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)

        for symbol in ["+", "-", "*", "/"]:
            button = Button(text=symbol)
            button.bind(on_press=self.calculate)
            layout.add_widget(button)

        self.result = Label(text="उत्तर येथे दिसेल")
        layout.add_widget(self.result)

        return layout

    def calculate(self, instance):
        try:
            a = float(self.num1.text)
            b = float(self.num2.text)
            op = instance.text

            if op == "+":
                answer = a + b
            elif op == "-":
                answer = a - b
            elif op == "*":
                answer = a * b
            elif op == "/":
                if b == 0:
                    self.result.text = "Cannot divide by zero"
                    return
                answer = a / b

            self.result.text = f"Answer: {answer:g}"

        except ValueError:
            self.result.text = "Enter both numbers"


CalculatorApp().run()
