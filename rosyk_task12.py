from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_string('''
<RootWidget>:
    orientation: 'vertical'
    x_input: x_input
    epsilon_input: epsilon_input
    result_label: result_label
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: '40sp'
        Label:
            text: 'Введіть значення x:'
        TextInput:
            id: x_input
            multiline: False
        Label:
            text: 'Введіть точність ε:'
        TextInput:
            id: epsilon_input
            multiline: False
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: '40sp'
        Button:
            text: 'Обчислити'
            on_press: root.calculate()
        Label:
            id: result_label
            text: ''
''')

class RootWidget(BoxLayout):
    x_input = ObjectProperty(None)
    epsilon_input = ObjectProperty(None)
    result_label = ObjectProperty(None)

    def calculate(self):
        try:
            x = float(self.x_input.text)
            epsilon = float(self.epsilon_input.text)
            y = 1 / (1 + x) ** 2
            total = 0
            n = 1
            while True:
                term = (-1) ** (n - 1) * n * x ** (n - 1)
                if abs(term) < epsilon:
                    break
                total += term
                n += 1
            self.result_label.text = f'Сума доданків: {total:.6f}'
        except ValueError:
            self.result_label.text = 'Невірно введені дані'

class MyApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MyApp().run()
