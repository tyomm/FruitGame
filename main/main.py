from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from random import randint
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.add_widget(Button(text="Start", size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.1}, on_press=self.pressed))

    def pressed(self, instance):
        print("Button Pressed!! !== meow ==!")
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.switch_to(SecondScreen())

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.add_widget(Image(source='main/watermelon.png', pos_hint={'center_x': 0.5, 'center_y': 0.5}))  # Here the image that we want to hit with knife

class MyScreenManager(ScreenManager):
    pass


class FruitGameApp(App):
    def build(self):
        global screen_manager
        screen_manager = MyScreenManager()
        screen_manager.add_widget(MainScreen(name="main"))
        return screen_manager


if __name__ == '__main__':
    FruitGameApp().run()
