from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

Builder.load_file('design.kv')

class MainScreen(Screen):
    def calculate(self, amp):
        self.ids.minutes.text = str(480 / float(amp) / 60) + " minutes"

    def go_to_dilute(self):
        self.manager.transition.direction = "left"
        self.manager.current = "dilute_screen"

class DiluteScreen(Screen):
    def go_to_main(self):
        self.manager.transition.direction = "right"
        self.manager.current = "main_screen"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
