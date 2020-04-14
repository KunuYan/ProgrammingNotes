import os, time
os.environ['KIVY_TEXT'] = 'pil'
import kivy
from kivy.app import App
from kivy.uix.button import Button


class HelloApp(App):

    def build(self):
        return Button(text='my first button')


if __name__ == '__main__':
    my_app = HelloApp()
    my_app.run()